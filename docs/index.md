---
layout: home
hero:
  name: Allie Cat Keebs
  text: Documentation
  tagline: Your comprehensive guide to Holykeebs keyboards powered by Allie Cat Keebs QMK firmware.
  actions:
    - theme: brand
      text: Get Started
      link: /guide/
---

<script setup>
import { VPFeatures } from 'vitepress/theme'
</script>

<VPFeatures
  :features="[
    { icon: '🐾', title: 'Setting Up Your Development Environment', details: 'Get your system ready for firmware development.', link: '/guide/setup_tooling' },
    { icon: '✨', title: 'Key Features and Modifications', details: 'Understand the unique aspects of this QMK fork.', link: '/guide/fork_features' },
    { icon: '🐈', title: 'Vial Integration', details: 'Learn how to use Vial for real-time keymap configuration.', link: '/guide/vial' },
    { icon: '⚙️', title: 'Building Your Firmware', details: 'Step-by-step instructions for compiling your firmware.', link: '/guide/building_firmware' },
    { icon: '🎨', title: 'HKS Driver Modifications', details: 'Dive into the specific driver changes and view automated call graphs.', link: '/guide/hks_driver_modifications' },
    { icon: '🚀', title: 'CI/CD Workflow', details: 'Understand our automated build and testing processes.', link: '/guide/ci_cd' },
    { icon: '🤝', title: 'Contributing to the Project', details: 'Guidelines for contributing to this repository.', link: '/guide/contributing' },
  ]"
/> 
