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
          { text: 'Setting Up Development Environment', link: '/guide/setup_tooling' },
          { text: 'HKS Driver Modifications', link: '/guide/hks_driver_modifications' },
          { text: 'Vial Integration', link: '/guide/vial' },
          { text: 'Building Your Firmware', link: '/guide/building_firmware' },
          { text: 'CI/CD Workflow', link: '/guide/ci_cd' },
          { text: 'Contributing to the Project', link: '/guide/contributing' },
          { text: 'Key Features and Modifications', link: '/guide/fork_features' },
          // Add other personal doc links here as needed
        ]
      },
      {
        text: 'HKS Driver Modifications',
        items: [
          { text: 'Azoteq Call Graph', link: '/azoteq_callgraph.svg' },
          { text: 'Cirque Call Graph', link: '/cirque_callgraph.svg' },
          { text: 'Pimoroni Call Graph', link: '/pimoroni_callgraph.svg' },
          { text: 'Trackpoint Call Graph', link: '/trackpoint_callgraph.svg' },
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
