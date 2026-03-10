VIA_ENABLE = yes
VIAL_ENABLE = yes
OLED_ENABLE = yes
MOUSEKEY_ENABLE = yes
EXTRAKEY_ENABLE = yes

# ---------------------------------------------------------------------------
# Pointing device — Cirque Pinnacle (ALLIE-201)
#
# Recommended: use the alliecatowo userspace (users/alliecatowo) which handles
# all sensor wiring automatically via POINTING_DEVICE + POINTING_DEVICE_POSITION.
# Example:
#   POINTING_DEVICE          = cirque40
#   POINTING_DEVICE_POSITION = right
#
# Standalone (no alliecatowo userspace): uncomment the lines below and choose the
# correct driver for your wiring (SPI or I2C).
# ---------------------------------------------------------------------------
# POINTING_DEVICE_ENABLE = yes
# POINTING_DEVICE_DRIVER = cirque_pinnacle_spi   # SPI wiring (MOSI/MISO/SCK/CS)
# POINTING_DEVICE_DRIVER = cirque_pinnacle_i2c   # I2C wiring (SDA/SCL)
