"""Generate changed site summaries locally. Requires the configured TTS environment and ffmpeg."""
import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path

os.environ.update(HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1', HF_HUB_DISABLE_TELEMETRY='1')
import numpy as np
import soundfile as sf
from mlx_audio.tts.utils import load_model

root = Path(__file__).resolve().parents[1]
manifest = root / 'docs/.vitepress/data/narration.json'
records = json.loads(manifest.read_text())
outdir = root / 'docs/public/narration'
outdir.mkdir(parents=True, exist_ok=True)
model = None
for item in records:
    output = outdir / (item['id'] + '.mp3')
    signature = hashlib.sha256((item['text'] + '|Kokoro-82M-bf16|af_heart|1.04|mp3-96k').encode()).hexdigest()
    if output.exists() and item.get('generationHash') == signature:
        print('Unchanged:', item['id'], flush=True)
        continue
    print('Generating:', item['id'], flush=True)
    existing = root / 'audio/ai-gaming-one-minute-final.wav'
    if item['id'] == 'explainer' and existing.exists() and item['text'].strip() == (root / 'examples/ai-gaming-one-minute.txt').read_text().strip():
        audio, sample_rate = sf.read(existing, dtype='float32')
    else:
        if model is None:
            model = load_model('mlx-community/Kokoro-82M-bf16')
        chunks = []
        for result in model.generate(text=item['text'], voice='af_heart', speed=1.04, lang_code='a'):
            chunks.append(np.asarray(result.audio, dtype=np.float32))
            sample_rate = result.sample_rate
        if not chunks:
            raise RuntimeError('No audio: ' + item['id'])
        audio = np.concatenate(chunks)
    if not np.isfinite(audio).all() or np.max(np.abs(audio)) == 0:
        raise RuntimeError('Invalid audio: ' + item['id'])
    seconds = len(audio) / sample_rate
    with tempfile.TemporaryDirectory() as temp:
        wav = Path(temp) / 'source.wav'
        mp3 = Path(temp) / 'encoded.mp3'
        sf.write(wav, audio, sample_rate, subtype='PCM_16')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(wav), '-codec:a', 'libmp3lame', '-b:a', '96k', str(mp3)], check=True)
        output.write_bytes(mp3.read_bytes())
    (outdir / (item['id'] + '.txt')).write_text(item['text'] + '\n')
    item['durationSeconds'] = round(seconds, 2)
    rounded = round(seconds)
    item['durationLabel'] = f'{rounded // 60}:{rounded % 60:02d}'
    item['generationHash'] = signature
    manifest.write_text(json.dumps(records, indent=2) + '\n')
    print(f"Saved {output.name}: {seconds:.1f} seconds", flush=True)
