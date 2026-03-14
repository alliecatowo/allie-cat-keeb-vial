# Optimizing Firmware Size

This prompt helps you reduce firmware size to fit within RP2040 flash constraints.

## Task Overview
Reduce compiled firmware size while maintaining core functionality.

## Current Constraints

- **Target**: RP2040 with 2MB flash
- **Warning threshold**: 1.5MB
- **Maximum**: ~2MB (minus bootloader)
- **Vial overhead**: Significant (dynamic keymaps, config storage)

## Size Optimization Strategy

### 1. Measure Current Size
```bash
# Build and check size
python build.py --build-single --left-device trackball --right-device tps43 --side left
ls -lh build_lily58/*.uf2
```

### 2. Identify Large Components

Check what's consuming space:
- Vial support (required)
- RGB matrix effects
- Console/debug output
- OLED features
- Dynamic keymap layers
- Pointing device drivers

### 3. Feature Reduction Priority

**High priority** (remove first):
- `CONSOLE_ENABLE = no`: Removes debug console (~10-20KB)
- `COMMAND_ENABLE = no`: Removes debug commands
- Reduce `DYNAMIC_KEYMAP_LAYER_COUNT`: Fewer layers = less RAM

**Medium priority**:
- `RGB_MATRIX_ENABLE = no`: Large savings if not needed
- Specific RGB effects: Disable individual effects
- `MOUSEKEYS_ENABLE = no`: If not using mouse keys
- `EXTRAKEY_ENABLE`: Consider if media keys are needed

**Low priority** (keep if possible):
- OLED support: Users often want this
- Pointing device support: Core feature
- Vial: Required for this fork

### 4. Compiler Optimizations

Enable these in rules.mk:
```makefile
LTO_ENABLE = yes              # Link Time Optimization
SPACE_CADET_ENABLE = no       # Save space if not used
GRAVE_ESC_ENABLE = no         # Save space if not used
MAGIC_ENABLE = no             # Save space if not used
```

### 5. Code-Level Optimizations

- Remove unused functions
- Minimize string constants
- Use const for read-only data
- Avoid large lookup tables
- Share code between configurations

## Configuration Template

For minimal Vial build:
```makefile
# Essential
VIAL_ENABLE = yes
POINTING_DEVICE_ENABLE = yes

# Optimize size
LTO_ENABLE = yes
CONSOLE_ENABLE = no
COMMAND_ENABLE = no
SPACE_CADET_ENABLE = no
GRAVE_ESC_ENABLE = no
MAGIC_ENABLE = no

# Reduce dynamic keymap
DYNAMIC_KEYMAP_LAYER_COUNT = 4

# Optional features (adjust as needed)
OLED_ENABLE = yes
RGB_MATRIX_ENABLE = no
MOUSEKEYS_ENABLE = no
```

## Testing After Optimization

1. Build firmware and verify size
2. Test all core features:
   - Key input works
   - Vial connectivity
   - Pointing device functionality
   - Layer switching
   - Any OLED displays
3. Flash to hardware and test thoroughly
4. Document what features were disabled

## Size Targets by Configuration

- **Minimal** (trackball only): ~600-800KB
- **Standard** (dual device + OLED): ~900KB-1.2MB
- **Full featured** (RGB + everything): ~1.5MB+

## Monitoring Size Over Time

Add size checks to CI:
```yaml
- name: Check firmware size
  run: |
    size=$(stat -c%s build_lily58/*.uf2 | head -1)
    echo "Firmware size: $size bytes"
    if [ $size -gt 1572864 ]; then
      echo "::error::Firmware too large!"
      exit 1
    fi
```

## Important Notes

- Don't sacrifice core Vial functionality
- Users expect pointing device support
- OLED is popular - try to keep it
- Debug builds are larger (acceptable for development)
- Release builds should be optimized
