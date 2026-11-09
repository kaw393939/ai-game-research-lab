<script setup>
import { computed, ref, onBeforeUnmount } from 'vue'
import { withBase } from 'vitepress'
import recordings from '../data/narration.json'
const props = defineProps({ id: { type: String, required: true } })
const recording = computed(() => recordings.find(item => item.id === props.id))
const player = ref(null)
const failed = ref(false)
function play() {
  document.querySelectorAll('audio').forEach(audio => {
    if (audio !== player.value) audio.pause()
  })
}
onBeforeUnmount(() => player.value?.pause())
</script>

<template>
  <section v-if="recording" class="audio-summary" :aria-label="`Audio summary: ${recording.title}`">
    <div class="audio-heading"><strong>Listen: {{ recording.title }}</strong><span>{{ recording.durationLabel || 'Audio summary' }}</span></div>
    <audio ref="player" controls preload="none" :aria-label="recording.title" :src="withBase(`/narration/${id}.mp3`)" @play="play" @error="failed = true">
      Your browser does not support audio playback. Use the download link below.
    </audio>
    <p v-if="failed" role="status">Audio could not load. Try the download link or read the transcript.</p>
    <div class="audio-links"><a :href="withBase(`/narration/${id}.mp3`)" download>Download MP3</a><a :href="withBase(recording.page.endsWith('/') ? recording.page : `${recording.page}.html`)">Read the page</a></div>
    <details><summary>Read transcript</summary><p>{{ recording.text }}</p></details>
    <small>Synthetic narration · Kokoro · Reviewed November 9, 2026</small>
  </section>
</template>

<style scoped>
.audio-summary { margin: 20px 0 28px; padding: 20px; border: 1px solid var(--vp-c-divider); border-radius: 14px; background: var(--vp-c-bg-soft); }
.audio-heading { display: flex; flex-wrap: wrap; gap: 8px 18px; justify-content: space-between; margin-bottom: 12px; }
.audio-heading span, small { color: var(--vp-c-text-2); }
audio { display: block; width: 100%; margin: 12px 0; }
.audio-links { display: flex; flex-wrap: wrap; gap: 8px 20px; font-size: 14px; }
details { margin: 12px 0; }
summary { cursor: pointer; font-weight: 500; }
small { display: block; font-size: 12px; }
</style>
