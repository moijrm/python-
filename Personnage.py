# classes
class Personnage:
    def __init__(self, nom, vie=100, degat=10):
        self.nom = nom
        self.vie = vie
        self.degat = degat

    def __str__(self):
        return f"Nom : {self.nom} | Vie : {self.vie} | Degat : {self.degat}"

    def attaquer(self, cible):
        cible.vie -= self.degat
        print(f"{self.nom} a infligé {self.degat} points de degat à {cible.nom}.")

    def en_vie(self):
        if self.vie > 0:
            return True
        else:
            print(f"{self.nom} est mort.")
            return False

class Guerrier(Personnage):
    def __init__(self, nom, vie=150, degat=15):
        super().__init__(nom, vie, degat)

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} avec son épée.")
        super().attaquer(cible)

class Mage(Personnage):
    def __init__(self, nom, vie=100, degat=8):
        super().__init__(nom, vie, degat)

    def attaquer(self, cible):
        print(f"{self.nom} lance un sort sur {cible.nom}.")
        super().attaquer(cible)

# fonctions
def affichage_choix():
    return (
        "----------------\n"
        "1. Créer un Guerrier\n"
        "2. Créer un Mage\n"
        "3. Afficher les personnages\n"
        "4. Faire combattre les Personnages\n"
        "5. Quitter\n"
        "----------------"
    )

def affichage_perso(persos):
    for p in persos:
        print(p)

def combat(a, b):
    print(f"\nCombat entre {a.nom} et {b.nom} !\n")
    while a.en_vie() and b.en_vie():
        a.attaquer(b)
        if b.en_vie():
            b.attaquer(a)
    print("Le combat est terminé !\n")

# programme principal
perso = []

while True:
    print(affichage_choix())
    try:
        choix = int(input("Votre choix : "))
    except:
        print("Donnez une valeur valide")
        continue

    if choix == 1:
        joueur = Guerrier(input("Donner un nom à votre Guerrier : "))
        perso.append(joueur)
    elif choix == 2:
        joueur1 = Mage(input("Donner un nom à votre Mage : "))
        perso.append(joueur1)
    elif choix == 3:
        affichage_perso(perso)
    elif choix == 4:
        if len(perso) < 2:
            print("Il faut au moins 2 personnages pour un combat !")
            continue
        print("Choisissez les personnages à combattre :")
        for idx, p in enumerate(perso):
            print(f"{idx}: {p.nom}")
        try:
            i = int(input("Premier personnage : "))
            j = int(input("Second personnage : "))
            combat(perso[i], perso[j])
        except:
            print("Index invalide !")
    elif choix == 5:
        print("Déconnexion")
        break
    else:
        print("Choix invalide")
