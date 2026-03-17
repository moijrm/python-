import requests

try:
    reponse = requests.get("https://wttr.in/Mons?format=j1")
    data = reponse.json()
    temperature = data["data"]["current_condition"][0]["temp_C"]
    print(f"Il fait {temperature}°C à Mons")

except requests.exceptions.ConnectionError as e:
    print(f"Erreur de connexion : {e}")
    