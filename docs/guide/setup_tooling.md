# Setting Up Your Development Environment

This guide will walk you through setting up the necessary tooling to build and develop your Allie Cat Keebs firmware. We will focus on using `uv` for Python dependency management and the `qmk` CLI tool for firmware building.

## Prerequisites

Before you begin, ensure you have:

*   **Git**: For cloning the repository and managing versions.
*   **Node.js & npm/Yarn**: Required for building the VitePress documentation.

## 1. Install `uv` (Python Package Manager)

`uv` is a fast and modern Python package installer and resolver. We recommend using it to manage your Python dependencies.

### macOS & Linux

To install `uv`, you can use the official installation script:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

This script will install `uv` into `~/.cargo/bin` (which should be in your PATH). If it's not, you'll need to add it:

```bash
# Add to your shell profile (e.g., ~/.zshrc, ~/.bashrc)
export PATH="$HOME/.cargo/bin:$PATH"
source ~/.zshrc # Or ~/.bashrc, etc.
```

### Windows

For Windows, you can install `uv` via `pip` (after installing Python) or by downloading the pre-built binary. We recommend using `pip`:

```bash
python -m pip install uv
```

## 2. Set up Python Virtual Environment with `uv`

It's highly recommended to use a virtual environment to isolate your project dependencies. Navigate to the root of your `qmk_firmware` repository and create a virtual environment:

```bash
cd /path/to/your/qmk_firmware
uv venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Now, install the project's Python dependencies:

```bash
uv pip install -r requirements.txt -r requirements-dev.txt
```

## 3. Install QMK Firmware CLI

The QMK Firmware CLI (`qmk`) is a powerful tool for managing and building QMK firmware. You can install it using `pip` within your activated `uv` virtual environment:

```bash
uv pip install qmk
```

After installation, you can set up the QMK environment:

```bash
qmk setup -y
```

## 4. Building Your Firmware

Once `uv` and `qmk` are set up, you can build your firmware. For detailed build instructions, refer to the [Building Your Own Firmware](../README.md#🛠️-building-your-own-firmware) section in the main `README.md`.

## 5. Building and Serving Documentation

To build and serve your custom documentation locally using VitePress:

1.  **Navigate to the `docs/` directory:**
    ```bash
    cd docs/
    ```

2.  **Install Node.js dependencies:**
    ```bash
    npm install
    # or yarn install if you use Yarn
    ```

3.  **Generate Call Graphs (from the repository root, ensuring `uv` environment is active, and then commit them):
    ```bash
    cd .. # Go back to repo root
    .venv/bin/python3 tools/callgraph.py --driver azoteq
    .venv/bin/python3 tools/callgraph.py --driver pimoroni
    .venv/bin/python3 tools/callgraph.py --driver cirque
    .venv/bin/python3 tools/callgraph.py --driver trackpoint
    # The generated SVGs are now in the docs/ directory and should be committed
    cd docs/ # Go back to docs directory
    ```

4.  **Start the VitePress development server:**
    ```bash
    npm run docs:dev
    # or yarn docs:dev if you use Yarn
    ```

This will launch the documentation site in your web browser. 
