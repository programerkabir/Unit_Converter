# 📏 Project 01: Unit Converter

A simple **Google-style Unit Converter** built using **Python** and **Streamlit**.

## Live Demo

[click here for live demo](https://unitconverter-kj5skkg4appwbwba84vkvgb.streamlit.app/)


## ScreenShoot

![image](https://github.com/user-attachments/assets/1f98f36d-55b7-4edc-8739-0cccd7543fc6)

## 🚀 Features
- Convert between **Metre** and **Centimetre**
- Real-time conversion
- Clean UI with interactive widgets
- Shows the formula used in conversion

## 🔁 Conversion Logic
```python
def convert_units(value, from_u, to_u):
    if from_u == "Metre" and to_u == "Centimetre":
        return value * 100
    elif from_u == "Centimetre" and to_u == "Metre":
        return value / 100
    else:
        return value
