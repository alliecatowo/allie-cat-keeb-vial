import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Allie Cat Keebs',
  ignoreDeadLinks: true,
  outDir: '../.build/docs', // This will output to qmk_firmware/.build/docs
  themeConfig: {
    // Manually define your sidebar here
    sidebar: [
      {
        text: 'Allie Cat\'s Docs',
        items: [
          // Assuming your personal markdown files are in docs/guide/
          { text: 'Overview', link: '/guide/overview' },
          { text: 'Features', link: '/guide/features' },
          { text: 'README', link: '/guide/README' },
          // Add other personal doc links here as needed
        ]
      },
      {
        text: 'Holykeebs Docs',
        items: [
          // Links to Holykeebs docs within the submodule.
          // The paths here should reflect the relative paths of the markdown files
          // within the `docs/holykeebs` submodule, as they will be transformed by VitePress.
          // For example, if holykeebs has a `docs/introduction.md`, it would be `/holykeebs/introduction`.
          // You may need to inspect the `docs/holykeebs` submodule to get the exact paths.
          { text: 'Holykeebs Home', link: '/holykeebs/' },
          // Add more specific holykeebs links here if known, e.g.:
          // { text: 'Holykeebs Guide', link: '/holykeebs/guide/some_page' },
        ]
      },
      {
        text: 'Official External Docs',
        items: [
          { text: 'Official Vial Docs', link: 'https://get.vial.today' },
          { text: 'Official Holykeebs Docs', link: 'https://docs.holykeebs.com' },
          { text: 'Official QMK Docs', link: 'https://docs.qmk.fm' }
        ]
      }
    ]
  }
})
