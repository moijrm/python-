import string
import random

#string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
#string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ 
#string.digits          # 0123456789 
#string.punctuation     # !"#$%&'()*+,-... 
while True:
    try:
        choix = int(input("longueur du mot de passe : "))
        break
    except ValueError:
        print("invalide")
    
maj = input("Ajouter Majuscule(o/n)")
chiffres = input("Ajouter chiffres (o/n)")
symbole = input("Ajouter Symbole (o/n)")

caracteres = string.ascii_lowercase  
if maj == "o":
    caracteres += string.ascii_uppercase  
if chiffres == "o":
    caracteres += string.digits  
if symbole == "o":
    caracteres += string.punctuation
    
mdp = ""
for i in range(choix):
    mdp += random.choice(caracteres)
print(mdp)

with open("motdepasse.txt" , "w") as f:
    f.write(mdp)
