import DefaultTheme from 'vitepress/theme'
import AudioSummary from '../components/AudioSummary.vue'
import './style.css'
export default {
  extends: DefaultTheme,
  enhanceApp({ app }) { app.component('AudioSummary', AudioSummary) }
}
