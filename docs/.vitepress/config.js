import { defineConfig } from 'vitepress'
import autoSidebar from './auto_sidebar.json' with { type: 'json' }

export default defineConfig({
  title: 'allie_cat_keeps',
  ignoreDeadLinks: true,
  themeConfig: {
    sidebar: [
      ...autoSidebar,
      {
        text: 'Links',
        items: [
          { text: 'Upstream QMK Docs', link: 'https://docs.qmk.fm' }
        ]
      }
    ]
  }
})
