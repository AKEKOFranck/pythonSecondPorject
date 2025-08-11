import requests
import random

response = requests.get('https://api.jikan.moe/v4/anime')

state = response.status_code

if state == 200:
    animeList = []
    output = response.json()
    for o in output['data']:
        animeSelect = o['title']
        animeList.append(animeSelect)
    animeChoices = random.choice(animeList)
    print(f"nous vous proposons comme animé : {animeChoices}")

else:
    print("message d'erreur" )
    
    
    """import requests
import random

class Anime:
    def __init__(self, name):
        name=""
        
    def choices(self):
        while
    """
