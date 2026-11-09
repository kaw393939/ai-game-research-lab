"""Generate a local Kokoro WAV from a text file. Downloads require --download."""
import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('input', type=Path)
p.add_argument('--output', type=Path, required=True)
p.add_argument('--voice', default='af_heart')
p.add_argument('--speed', type=float, default=1.0)
p.add_argument('--download', action='store_true', help='Allow first-run model downloads')
p.add_argument('--force', action='store_true')
args = p.parse_args()
if args.output.exists() and not args.force:
    p.error('Output already exists; use a new name or --force.')
if args.speed <= 0:
    p.error('Speed must be positive.')
text = args.input.read_text().strip()
if not text:
    p.error('Input file is empty.')
os.environ['HF_HUB_DISABLE_TELEMETRY'] = '1'
if not args.download:
    os.environ['HF_HUB_OFFLINE'] = '1'
    os.environ['TRANSFORMERS_OFFLINE'] = '1'
import spacy
if not args.download and not spacy.util.is_package('en_core_web_sm'):
    p.error('English text model is missing. Run once with --download.')
import numpy as np
import soundfile as sf
from mlx_audio.tts.utils import load_model
model = load_model('mlx-community/Kokoro-82M-bf16')
chunks = []
sample_rate = None
for result in model.generate(text=text, voice=args.voice, speed=args.speed, lang_code='a'):
    chunks.append(np.asarray(result.audio, dtype=np.float32))
    sample_rate = result.sample_rate
if not chunks:
    raise RuntimeError('Model produced no audio.')
waveform = np.concatenate(chunks)
if not np.isfinite(waveform).all() or np.max(np.abs(waveform)) == 0:
    raise RuntimeError('Model produced invalid or silent audio.')
args.output.parent.mkdir(parents=True, exist_ok=True)
sf.write(str(args.output), waveform, sample_rate, subtype='PCM_16')
print(f'Saved {args.output.resolve()} ({len(waveform) / sample_rate:.2f} seconds, {sample_rate} Hz)')
