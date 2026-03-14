# Adding a New Pointing Device Configuration

This prompt helps you add support for a new pointing device configuration to the build system.

## Task Overview
Add support for a new pointing device configuration to build.py and ensure it can be built successfully.

## Steps to Follow

1. **Understand the current configuration**:
   - Review `build.py` to see how existing devices are configured
   - Check `users/holykeebs/rules.mk` for device-specific build rules
   - Look at existing device drivers in `drivers/sensors/`

2. **Add the new configuration**:
   - Update `build.py` to include the new device in the valid configurations
   - Modify the build matrix if needed
   - Ensure proper naming conventions are followed

3. **Create necessary drivers** (if new hardware):
   - Add driver files to `drivers/sensors/`
   - Update `users/holykeebs/rules.mk` to include new drivers
   - Follow existing driver patterns for initialization and polling

4. **Update documentation**:
   - Update README.md with new configuration options
   - Document any special requirements or setup steps

5. **Test thoroughly**:
   - Build firmware for the new configuration
   - Verify firmware size is within limits
   - Test on actual hardware if available

## Important Considerations

- **Memory constraints**: RP2040 has limited flash (2MB)
- **Compatibility**: Ensure it works with Vial
- **Build matrix**: Update CI configuration if needed
- **Documentation**: Users need clear instructions

## Example Configuration

For reference, existing configurations include:
- `trackball`: Pimoroni trackball with RGB
- `tps43`: Azoteq IQS5xx TPS43 touchpad
- `trackpoint`: PS2 trackpoint modules
- Dual configurations: `trackball_tps43`, `trackball_trackpoint`, etc.
