# Contributing to the Project

We welcome contributions to this project! Whether you're fixing a bug, adding a new keyboard, improving documentation, or suggesting a new feature, your help is greatly appreciated. This guide outlines the process for contributing to ensure a smooth and efficient collaboration.

## Before You Start

*   **Read the `readme.md`**: Familiarize yourself with the project's overview and basic setup.
*   **Set up your Development Environment**: Follow the instructions in [Setting Up Development Environment](/guide/setup_tooling) to ensure you have all necessary tools installed.
*   **Understand the Build Process**: Review [Building Your Firmware](/guide/building_firmware) to understand how firmware is compiled.
*   **Review Existing Issues**: Check the [GitHub Issues](https://github.com/holykeebs/qmk_firmware/issues) to see if your idea or bug has already been reported or is being worked on.

## Contribution Workflow

We use the standard GitHub Flow for contributions:

1.  **Fork the Repository**: Start by forking the `holykeebs/qmk_firmware` repository to your GitHub account.

2.  **Clone Your Fork**: Clone your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/qmk_firmware.git
    cd qmk_firmware
    ```

3.  **Create a New Branch**: Create a new branch for your changes. Use a descriptive name:
    ```bash
    git checkout -b feature/my-new-feature
    # or for a bug fix
    git checkout -b bugfix/fix-issue-123
    ```

4.  **Make Your Changes**: Implement your changes, whether it's code, documentation, or new configurations.

    *   **Code Style**: Adhere to the existing code style. Run linters if applicable.
    *   **Testing**: Thoroughly test your changes. Build your firmware ([Building Your Firmware](/guide/building_firmware)) and flash it to your keyboard to verify functionality.
    *   **Documentation**: If your changes affect functionality or add new features, update the relevant documentation. If you're adding a new keyboard, ensure its documentation is complete.
    *   **Call Graphs**: If your changes involve driver modifications, ensure that `tools/callgraph.py` is run and the generated SVGs are updated and committed. This is handled automatically by the CI/CD, but it's good practice to verify locally.

5.  **Commit Your Changes**: Commit your changes with a clear and concise commit message. If your commit addresses a specific issue, reference it using `Fixes #123` or `Closes #456`.
    ```bash
    git add .
    git commit -m "feat: Add new feature for X"
    ```

6.  **Push to Your Fork**: Push your new branch to your forked repository on GitHub:
    ```bash
    git push origin feature/my-new-feature
    ```

7.  **Create a Pull Request (PR)**: Go to your forked repository on GitHub and open a new Pull Request. 

    *   **Title**: Provide a clear and descriptive title for your PR.
    *   **Description**: Explain the purpose of your changes, what problem they solve, and any relevant details. Include screenshots or GIFs if appropriate.
    *   **Link to Issues**: If your PR addresses an issue, link to it in the description.

## Code Review

Once your PR is opened, it will undergo an automated CI/CD check ([CI/CD Workflow](/guide/ci_cd)). If all checks pass, a maintainer will review your code. Be prepared to address any feedback or requests for changes.

## Important Notes

*   **Keep PRs Small**: Aim for small, focused pull requests that address a single issue or feature. This makes reviews easier and faster.
*   **Be Responsive**: Try to respond to comments and requests from reviewers in a timely manner.
*   **Be Patient**: Review times can vary. Your patience is appreciated.
*   **Sync with Upstream**: Periodically rebase your branch on the `main` branch of the upstream repository to avoid merge conflicts:
    ```bash
    git fetch upstream
    git rebase upstream/main
    ```

Thank you for contributing to this project! 
