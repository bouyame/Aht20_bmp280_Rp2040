# 🌡️💧📟 Aht20_bmp280_Rp2040  
**Lecture des capteurs BMP280 et AHT10 avec écran OLED SH1106( SSD1306) en MicroPython (RP2040)**

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

---

## ▶️ Utilisation  

1. Flashez MicroPython sur votre Raspberry Pi Pico.  
2. Copiez tous les fichiers `.py` dans le système de fichiers du Pico (via Thonny, rshell, ou autre).  
3. Exécutez `main.py` : les mesures s’affichent en direct sur l’écran OLED.

---


## 👤 Auteur  
**Mohamed Bouya**  
Projet open-source sous licence libre.  
Vous êtes libre de modifier, améliorer et partager !

---

## 📜 Licence  
Ce projet est sous licence MIT – voir le fichier `LICENSE` pour plus d'informations.



