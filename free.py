import requests

store = {"1": "steam" , "25" : "Epic Games Store"}

try:
    message = requests.get("https://www.cheapshark.com/api/1.0/deals?upperPrice=0")
    data = message.json()

    for jeu in data:
        print(jeu["title"])
        if jeu["steamRatingText"] is None:
            print("pas de note")
        else:
            print(jeu["steamRatingText"])
        print(store[jeu["storeID"]])

        if jeu["storeID"] == "1":
            print(f"https://store.steampowered.com/app/{jeu["gameID"]}")
        elif jeu["storeID"] == "25":
            print(f"https://store.epicgames.com/fr/p/{jeu["internalName"].lower()}")
        print("--------")
        
except requests.exceptions.RequestException as e:
    print(f"Erreur de connexion : {e}")