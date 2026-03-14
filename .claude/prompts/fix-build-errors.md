# Fixing Build Errors

This prompt helps you systematically debug and fix build errors in the QMK firmware.

## Task Overview
Diagnose and fix compilation errors when building firmware.

## Common Build Error Categories

### 1. Missing Dependencies
**Symptoms**: "command not found", "cannot find -l"
**Solutions**:
- Install QMK dependencies: `pip3 install -r requirements.txt`
- Install ARM GCC toolchain: `gcc-arm-none-eabi`
- Check submodules: `git submodule update --init --recursive`

### 2. Vial Integration Issues
**Symptoms**: Vial-specific errors, keycode issues
**Solutions**:
- Ensure `VIAL_ENABLE=yes` is passed to make
- Check vial.json exists in keymap directory
- Verify Vial version compatibility

### 3. Memory Overflow
**Symptoms**: "region `FLASH' overflowed", firmware too large
**Solutions**:
- Disable optional features (CONSOLE, RGB effects)
- Optimize feature selection in rules.mk
- Check for duplicate code or large arrays
- Use LTO (Link Time Optimization)

### 4. Pointing Device Errors
**Symptoms**: Driver compilation errors, undefined references
**Solutions**:
- Verify POINTING_DEVICE is set correctly
- Check driver includes in users/holykeebs/rules.mk
- Ensure device-specific config in config.h

### 5. Missing Symbols
**Symptoms**: "undefined reference to", "implicit declaration"
**Solutions**:
- Check header includes
- Verify function signatures match declarations
- Ensure source files are included in compilation

## Debugging Process

1. **Read the error message carefully**:
   - Note the file and line number
   - Identify the actual error vs. cascade errors

2. **Isolate the issue**:
   - Try building a simpler configuration
   - Disable recent changes to find the breaking change

3. **Check recent changes**:
   - Review git diff to see what changed
   - Test reverting suspicious changes

4. **Verify environment**:
   - Ensure toolchain is up to date
   - Check QMK version and submodules

5. **Build with verbose output**:
   - Add `-v` flag to see full compilation commands
   - Check for warnings that might indicate issues

6. **Test incrementally**:
   - Fix one error at a time
   - Rebuild after each fix

## Memory Optimization Techniques

If firmware is too large:
1. Disable CONSOLE_ENABLE
2. Reduce RGB effects or disable RGB_MATRIX
3. Minimize DYNAMIC_KEYMAP_LAYER_COUNT
4. Disable unused features (AUDIO, MOUSEKEYS, etc.)
5. Enable LTO_ENABLE for smaller binary

## Getting Help

If stuck:
- Check QMK Discord #firmware-help
- Review similar issues in GitHub
- Provide full error output and build command
- Mention the specific configuration being built
