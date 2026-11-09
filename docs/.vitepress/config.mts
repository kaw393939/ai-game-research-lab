import { defineConfig } from 'vitepress'
export default defineConfig({
  title: 'AI Game Research Lab',
  description: 'Testing the boundaries of AI-assisted game creation through reproducible experiments.',
  base: '/ai-game-research-lab/',
  lang: 'en-US',
  lastUpdated: true,
  themeConfig: {
    nav: [{ text: 'Research', link: '/research/' }, { text: 'Experiments', link: '/experiments/' }, { text: 'Roadmap', link: '/roadmap' }],
    sidebar: [
      { text: 'The lab', items: [{ text: 'Mission & method', link: '/guide' }, { text: 'Research map', link: '/research/' }, { text: 'Roadmap', link: '/roadmap' }] },
      { text: 'Research tracks', items: [{ text: 'Programming & agents', link: '/research/programming' }, { text: 'Audio & voice', link: '/research/audio' }, { text: '3D models & animation', link: '/research/3d' }, { text: 'Game integration', link: '/research/integration' }, { text: 'REA: reverse engineering', link: '/research/rea' }] },
      { text: 'Evidence', items: [{ text: 'Experiment register', link: '/experiments/' }, { text: 'Experiment template', link: '/experiments/template' }, { text: 'Decision log', link: '/decisions' }] }
    ],
    socialLinks: [{ icon: 'github', link: 'https://github.com/kaw393939/ai-game-research-lab' }],
    search: { provider: 'local' },
    editLink: { pattern: 'https://github.com/kaw393939/ai-game-research-lab/edit/main/docs/:path' },
    footer: { message: 'Build small. Measure honestly. Publish what we learn.' }
  }
})
