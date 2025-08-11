import requests
import random

response = requests.get('https://api.jikan.moe/v4/anime')
state = response.status_code
animeList = []
if state == 200:
    while True:
        user = input("Entrez C/c pour générer un titre ou Q/q pour quitter : ").strip().lower()

        # Vérifie que l'entrée est valide (seulement 'c' ou 'q')
        while user not in ('c', 'q'):
            print("Erreur : Entrée non valide. Veuillez choisir C/c ou Q/q.")
            user = input("Entrez C/c pour générer un titre ou Q/q pour quitter : ").strip().lower()

        if user == 'c':
            output = response.json()
            animeList = [o['title'] for o in output['data']]  # Remplissage unique de la liste
            animeChoices = random.choice(animeList)
            print(f"Nous vous proposons comme animé : {animeChoices}")

        elif user == 'q':
            print("Profitez bien de votre animé du jour !")
            break
else:
    print("Erreur : Impossible de récupérer les données de l'API.")