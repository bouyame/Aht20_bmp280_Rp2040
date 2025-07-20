# 🌡️💧📟 Aht20_bmp280_Rp2040  
**Lecture des capteurs BMP280 et AHT10 avec écran OLED SH1106 en MicroPython (RP2040)**

---

## 📖 Description  
Ce projet en **MicroPython** permet de lire et d'afficher en temps réel les données de **température**, **pression** et **humidité** à l’aide des capteurs **BMP280** et **AHT10**, avec affichage sur un écran **OLED SH1106**.  
Il est basé sur une carte **Raspberry Pi Pico (RP2040)**.

---

## 🧰 Matériel nécessaire  

- [x] Raspberry Pi Pico (RP2040)  
- [x] Capteur **BMP280** (pression + température)  
- [x] Capteur **AHT10** ou **AHT20** (humidité + température)  
- [x] Écran **OLED SH1106** (I2C, 128x64)  
- [x] Fils Dupont  

---

## 🔌 Schéma de câblage

| Module      | GPIO Pico |
|-------------|------------|
| OLED SDA    | GP20       |
| OLED SCL    | GP21       |
| BMP280 SDA  | GP14       |
| BMP280 SCL  | GP15       |
| GND         | GND        |
| VCC         | 3.3V       |

> 💡 Note : Les capteurs utilisent l’interface **I2C**. Vous pouvez adapter les GPIO selon vos besoins.

---

## 🗂️ Structure du projet

Aht20_bmp280_Rp2040/
├── main.py # Boucle principale : lecture + affichage
├── aht10.py # Bibliothèque pour le capteur AHT10
├── bmp280.py # Bibliothèque pour le capteur BMP280
├── sh1106.py # Pilote de l'écran OLED SH1106
└── code_sh1106.py # Script de test de l’écran OLED
