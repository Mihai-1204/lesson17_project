import json

import requests

from main import get_config


def get_info(url: str, character: str):
    character = character.replace(" ", "%20")
    response = requests.get(url + f"?name={character}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data[0]['born']

if __name__ == '__main__':
    config = get_config()
    while True:
        name = input("Citeste un nume:")
        year_of_birth = get_info(config['url2'], character="Jon Snow")
        print(year_of_birth)