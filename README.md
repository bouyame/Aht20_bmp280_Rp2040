# Aht20_bmp280_Rp2040
Lecture des capteurs BMP280 et AHT20 avec OLED SH1106 en MicroPython
# Capteurs BMP280 + AHT10 + OLED SH1106 en MicroPython (RP2040)

Ce projet lit les données de température, pression et humidité à l'aide de :
- 🌡 BMP280
- 💧 AHT10
- 📟 Écran OLED SH1106

## Schéma de câblage

| Module     | Pico GPIO |
|------------|-----------|
| OLED SDA   | GP0       |
| OLED SCL   | GP1       |
| BMP SDA    | GP2       |
| BMP SCL    | GP3       |
| GND        | GND       |
| VCC        | 3.3V      |

## Fichiers
- `main.py` : boucle principale
- `aht10.py` : bibliothèque AHT10
- `bmp280.py` : bibliothèque BMP280
- `sh1106.py` : pilote écran OLED
-  code _sh1106.py :test écran oled sh1106 
## Auteur
- [Bouya Mohamed](https://github.com/bouyame)
