# Holykeebs QMK Firmware: Key Features and Modifications

This repository is an opinionated fork of the QMK Firmware designed specifically for Holykeebs keyboards. While it builds upon the robust foundation of QMK, it incorporates several key modifications and features tailored to the Holykeebs ecosystem, aiming for a streamlined and enhanced user experience.

## Core Philosophy

The primary goal of this fork is to provide a curated and optimized firmware experience for Holykeebs users. This includes:

*   **Targeted Keyboard Support**: Focus on Holykeebs keyboards, ensuring high-quality and tested firmware.
*   **Integrated Tooling**: Seamless integration with development tools like `uv` and automated processes.
*   **Streamlined Documentation**: Comprehensive and easy-to-follow documentation, including dynamically generated content.
*   **Vial First**: Prioritizing Vial compatibility for real-time keymap configuration.

## Key Modifications and Features

### 1. Vial Integration and Dependency Management

This fork maintains up-to-date Vial integration, often incorporating the latest changes and bug fixes from Vial upstream before they are widely available in the main QMK branch. This ensures that Holykeebs users benefit from the most recent Vial features and stability improvements.

Furthermore, the repository actively manages its QMK dependencies to ensure compatibility and leverage the latest stable QMK features. This helps in providing a reliable and feature-rich firmware without encountering issues due to outdated components.

For more details on Vial, refer to the [Vial Integration](/guide/vial) guide.

### 2. Automated Call Graph Generation

One of the unique features of this fork is the automated generation of driver modification call graphs. These visual representations help in understanding the specific changes made to drivers like Azoteq, Pimoroni, Cirque, and PS2 Trackpoint to suit Holykeebs hardware.

The `tools/callgraph.py` script automatically generates these SVG diagrams, which are then committed directly to the `docs/` directory by the CI/CD pipeline. This ensures that the documentation always has the most current and accurate visualizations of driver interactions.

For a detailed explanation and to view the generated call graphs, please see [HKS Driver Modifications](/guide/hks_driver_modifications).

### 3. Streamlined Build Process

The `build.py` script has been refined to simplify the firmware compilation process for Holykeebs keyboards. It provides easy-to-use options for building specific keyboards, all keyboards, Vial-compatible firmware, and release versions.

This script is also tightly integrated with the CI/CD pipeline, ensuring consistent and automated builds across the development lifecycle.

Learn more about building your firmware in [Building Your Firmware](/guide/building_firmware).

### 4. Comprehensive CI/CD Workflow

The Continuous Integration and Continuous Deployment (CI/CD) pipeline is a cornerstone of this project. It automates:

*   **Pull Request Checks**: Ensures code quality, linting, and successful compilation for all proposed changes.
*   **Automated Builds**: Regularly compiles and tests firmware for all supported keyboards.
*   **Documentation Generation**: Automatically updates and commits dynamically generated documentation assets, such as the call graphs.

This robust CI/CD setup helps maintain a high standard of code quality, reduces manual effort, and ensures that the documentation is always synchronized with the codebase.

Refer to the [CI/CD Workflow](/guide/ci_cd) guide for a detailed understanding of the automated processes.

### 5. Opinionated Documentation Structure

This repository utilizes VitePress for its documentation, providing a clear, concise, and easy-to-navigate resource for users and contributors. The documentation is designed to be self-sufficient, covering setup, building, testing, and troubleshooting specific to Holykeebs firmware.

The structure prioritizes practical guides and deep dives into Holykeebs-specific modifications, while also linking to official QMK, Vial, and Holykeebs documentation for broader context.

## Contributing

We encourage contributions! If you have ideas for improvements, bug fixes, or new features, please refer to the [Contributing to the Project](/guide/contributing) guide to get started. Your contributions help make this firmware even better for the Holykeebs community. 
