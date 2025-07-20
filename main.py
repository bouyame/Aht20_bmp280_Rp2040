from machine import Pin, I2C
import time
from sh1106 import SH1106_I2C
from bmp280 import BMP280
from aht10 import AHT10  # depuis ton fichier

# ---- Initialisation I2C ----
i2c_oled = I2C(0, scl=Pin(21), sda=Pin(20))      # OLED
i2c_sensors = I2C(1, scl=Pin(15), sda=Pin(14))   # AHT10 + BMP280

# ---- Afficher les périphériques I2C détectés ----
print("I2C0 (OLED) devices:", i2c_oled.scan())      # Ex: [60]
print("I2C1 (Sensors) devices:", i2c_sensors.scan())  # Ex: [56, 119]

# ---- Initialisation des modules ----
oled = SH1106_I2C(128, 64, i2c_oled, addr=0x3C)
bmp = BMP280(i2c_sensors, addr=0x77)
aht = AHT10(i2c_sensors, address=0x38)

# ---- Boucle de lecture et affichage ----
while True:
    try:
        t_bmp = bmp.temperature
        p_bmp = bmp.pressure
        t_aht, h_aht = aht.read()

        if t_aht is None:
            print("Erreur lecture AHT10")
            continue

        oled.fill(0)
        oled.text("T_BMP280: {:.1f} C".format(t_bmp), 0, 10)
        oled.text("Pr: {:.0f} hPa".format(p_bmp), 0, 20)
        oled.text("T_AHT10: {:.1f} C".format(t_aht), 0, 40)
        oled.text("Hum: {:.0f}%".format(h_aht), 0, 50)
        oled.show()

    except Exception as e:
        print("Erreur capteurs :", e)

    time.sleep(2)
