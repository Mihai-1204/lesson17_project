import json
import random
import time

import requests



def get_character_by_id(url: str, char_id: int):
    response = requests.get(f"{url}/{char_id}")
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def game_loop(url: str):
    score = 0
    game_data = {"score": score, "end_time": "", "characters_guessed": 0}

    while True:
        char_id = random.randint(1, 999)
        character = get_character_by_id(url, char_id)
        if character:
            alias = character.get('alias', 'No alias available')
            titles = character.get('titles', [])
            if alias == "No alias available" and not titles:
                continue

            print(f"Alias: {alias}")
            print(f"Titles: {', '.join(titles)}")

            guess = input("Guess the character's name: ").strip()
            if guess.lower() == character['name'].lower():
                print("Correct")
                score += 1
                game_data["characters_guessed"] += 1
            else:
                print(f"Wrong, the correct answer was {character['name']}")

        continue_game = input("Continue Y/N: ")
        if continue_game == 'n,N':
            game_data['end_time'] = str(time.time())
            game_data['score']  = score

            with open("game_data.json", "w") as f:
                json.dumps(game_data, f, indent=4)
            break


if __name__ == '__main__':
    url = "https://anapioficeandfire.com/api/characters"
    game_loop(url)
