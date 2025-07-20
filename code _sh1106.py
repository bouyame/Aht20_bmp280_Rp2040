from machine import Pin, I2C
from sh1106 import SH1106_I2C
import time

# Configuration I2C : SDA = GP0, SCL = GP1
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100_000)

# Scanner l'adresse I2C
devices = i2c.scan()
if not devices:
    print("Aucun périphérique I2C détecté !")
else:
    print("Périphériques I2C détectés :", devices)
    addr = devices[0]  # Prend le premier trouvé, souvent 0x3C
    oled = SH1106_I2C(128, 64, i2c, addr)

    oled.fill(0)
    oled.text("SH1106 OK!", 10, 10)
    oled.text("RP2040 MicroPython", 0, 30)
    oled.show()
