# Building Your Firmware

This guide provides detailed instructions on how to build the firmware for your Holykeebs-compatible keyboard using the provided `build.py` script. This script simplifies the compilation process and offers various options for different build targets.

## Prerequisites

Before you begin, ensure you have set up your development environment as described in the [Setting Up Development Environment](/guide/setup_tooling) guide.

## The `build.py` Script

The `build.py` script is a versatile tool designed to streamline the firmware compilation process. It handles dependency management, build configuration, and output generation.

### Basic Usage

To build the default firmware for a trackball-enabled keyboard (e.g., `trackball_tps43`), simply run:

```bash
.venv/bin/python3 build.py
```

### Building for a Single Keyboard

To build firmware for a specific keyboard and configuration, use the `--build-single` flag, specifying the `keyboard` and `keymap`:

```bash
.venv/bin/python3 build.py --build-single --keyboard crkbd --keymap default
```

Replace `crkbd` with your keyboard's name and `default` with your desired keymap. You can find available keyboard and keymap names by exploring the `keyboards/` directory.

### Building All Keyboards

To build firmware for all supported keyboards and their default keymaps, use the `--build-all` flag:

```bash
.venv/bin/python3 build.py --build-all
```

This process can take a significant amount of time, as it compiles firmware for every defined keyboard.

### Building Vial-Compatible Firmware

As discussed in the [Vial Integration](/guide/vial) guide, you can build a Vial-compatible firmware using the `--vial-only` flag:

```bash
.venv/bin/python3 build.py --vial-only
```

### Building for Release

To create a release build, which may include specific optimizations or versioning, use the `--release` flag:

```bash
.venv/bin/python3 build.py --release
```

### Generating Build Matrix (for CI/CD)

The `build.py` script can also generate a build matrix, which is particularly useful for continuous integration (CI/CD) pipelines. This is used to define which firmware configurations should be built.

```bash
.venv/bin/python3 build.py --generate-matrix-release --variants-file variants.json
```

This command will output a JSON string that CI/CD systems can parse to dynamically create build jobs.

## Build Output

Successfully built firmware files (`.uf2`, `.hex`, etc.) will be located in the `.build/` directory at the root of the repository. These are the files you will flash to your keyboard.

## Testing Your Firmware

After building your firmware, you should test it thoroughly. This typically involves:

1.  **Flashing the firmware** to your keyboard. Refer to the [QMK Firmware Flashing Guide](https://docs.qmk.fm/#/newbs_flashing) for general instructions.
2.  **Testing all keys and layers** to ensure they function as expected.
3.  **Verifying special features** like RGB lighting, encoders, and macros.
4.  **Using the Vial client** (if applicable) to confirm real-time configuration works.

If you encounter any issues, double-check your keymap configuration and the build process. For debugging, you can use QMK's built-in debugging features or refer to the QMK documentation. 
