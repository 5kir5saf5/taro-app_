import os
import requests

cards = {
    "fool": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_00_fool.jpg",
    "magician": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_01_magician.jpg",
    "high_priestess": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_02_high_priestess.jpg",
    "empress": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_03_empress.jpg",
    "emperor": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_04_emperor.jpg",
    "hierophant": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_05_hierophant.jpg",
    "lovers": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_06_lovers.jpg",
    "chariot": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_07_chariot.jpg",
    "strength": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_08_strength.jpg",
    "hermit": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_09_hermit.jpg",
    "wheel_of_fortune": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_10_wheel_of_fortune.jpg",
    "justice": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_11_justice.jpg",
    "hanged_man": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_12_hanged_man.jpg",
    "death": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_13_death.jpg",
    "temperance": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_14_temperance.jpg",
    "devil": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_15_devil.jpg",
    "tower": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_16_tower.jpg",
    "star": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_17_star.jpg",
    "moon": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_18_moon.jpg",
    "sun": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_19_sun.jpg",
    "judgement": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_20_judgement.jpg",
    "world": "https://raw.githubusercontent.com/ekelen/tarot-api/master/static/cards/rws_tarot_21_world.jpg"
}

os.makedirs("cards", exist_ok=True)

for name, url in cards.items():

    response = requests.get(url)

    with open(f"cards/{name}.jpg", "wb") as file:
        file.write(response.content)

    print(f"Скачано: {name}.jpg")

print("\nВсе карты скачаны в папку cards")