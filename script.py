import json

import requests
from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

API_URL = "https://akabab.github.io/superhero-api/api/all.json"

def find_tallest_hero(gender: Gender, has_job: bool):
    tallest_hero = {}
    max_height = 0.0

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        for hero in data:

            if gender.value != hero.get('appearance', {}).get('gender'):
                continue

            occupation = hero.get('work', {}).get('occupation', '-')
            has_occupation = occupation != '-'
            if has_job != has_occupation:
                continue

            height = hero.get('appearance', {}).get('height', ["-", "-"])

            if height[0] != "-" and "'" in height[0]:
                try:
                    ft_str, inch_str = height[0].split("'", 1)
                    feet = float(ft_str) if ft_str.strip() else 0

                    inch_part = inch_str.replace('"', '').replace("'", '').strip()
                    inches = float(inch_part) if inch_part else 0
                    height_cm = feet * 30.48 + inches * 2.54

                    if height_cm > max_height:
                        max_height = height_cm
                        tallest_hero = hero
                except ValueError:
                    print(f"Ошибка парсинга роста (футы/дюймы) для героя {hero.get('id')}")
                    continue

            if height[1] != "-":
                try:
                    if "cm" in height[1]:
                        height_cm = float(height[1].replace("cm", "").strip())
                    elif "meters" in height[1]:
                        height_cm = 100 * float(height[1].replace("meters", "").strip())
                    else:
                        continue

                    if height_cm > max_height:
                        max_height = height_cm
                        tallest_hero = hero
                except ValueError:
                    print(f"{hero.get('id')}")
                    continue

    except ValueError as e:
        print(e)
        return {}

    return tallest_hero

if __name__ == "__main__":
    print(json.dumps(find_tallest_hero(Gender.MALE, True)))