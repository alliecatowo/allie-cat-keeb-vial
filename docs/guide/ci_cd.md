# Continuous Integration and Continuous Deployment (CI/CD)

This repository leverages GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD) to automate the building, testing, and deployment of firmware. This ensures that all changes are thoroughly validated and that up-to-date firmware is always available.

## Overview of CI/CD Workflow

The CI/CD pipeline is defined in the `.github/workflows/` directory and consists of several automated workflows:

*   **`pr-checks.yml`**: Runs essential checks on every Pull Request (PR) to ensure code quality and prevent regressions.
*   **`build-firmware.yml`**: Builds firmware for all supported keyboards when changes are merged to the `main` branch or on a schedule.

## `pr-checks.yml` - Pull Request Checks

This workflow is triggered on every pull request to the `main` branch. Its primary goal is to provide rapid feedback to developers on the quality and correctness of their changes before they are merged.

Key steps in `pr-checks.yml`:

1.  **Setup Environment**: Installs necessary tools and sets up the Python virtual environment.
2.  **Linting**: Runs code linters to enforce coding style and identify potential errors.
3.  **Build Matrix Generation**: Uses `build.py --generate-matrix-release` to create a dynamic build matrix for various firmware configurations. This ensures that a wide range of firmware variations are tested.
4.  **Firmware Build**: For each configuration in the generated matrix, the workflow attempts to build the firmware using `build.py --build-single`. This step verifies that the changes do not break the compilation process for any supported keyboard.
5.  **Call Graph Generation**: The workflow runs `tools/callgraph.py` to generate updated SVG call graphs. These graphs are then committed to the `docs/` directory. This ensures that the documentation always reflects the latest driver modification visualizations. For more details on driver modifications and call graphs, refer to [HKS Driver Modifications](/guide/hks_driver_modifications).

If any of these steps fail, the PR cannot be merged, prompting the developer to address the issues.

## `build-firmware.yml` - Release Builds

This workflow is responsible for generating release-ready firmware. It is triggered upon merges to the `main` branch and periodically (e.g., daily) to ensure fresh builds.

Key steps in `build-firmware.yml`:

1.  **Similar to PR checks**: It performs environment setup, build matrix generation, and firmware compilation, similar to `pr-checks.yml`.
2.  **Artifact Upload**: After successful compilation, the generated `.uf2` firmware files (and other formats) are uploaded as build artifacts. These artifacts can then be downloaded and used by end-users.

## Call Graph Generation in CI/CD

As mentioned, the call graphs for driver modifications are an integral part of the documentation and are automatically generated during the CI/CD process. The `tools/callgraph.py` script is executed, and the resulting SVG files are committed directly to the `docs/` directory. This ensures that anyone viewing the documentation, whether locally or online, sees the most current visualizations.

This automation eliminates the need for manual generation and commitment of these assets, reducing human error and keeping the documentation synchronized with the codebase. 
