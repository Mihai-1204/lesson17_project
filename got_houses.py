import json
import requests




def get_houses_and_leaders(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        houses_data = json.loads(response.text)
        for house in houses_data:
            house_name = house['name']
            leader_name = house['currentLord']
            print(f"House: {house_name}")
            if leader_name:
                print(f"Leader: {leader_name}")
            else:
                print("No current leader")
            print("_" * 20)



if __name__ == '__main__':
    url = "https://anapioficeandfire.com/api/houses"
    get_houses_and_leaders(url)