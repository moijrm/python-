class Compte:
    def __init__(self, nom , solde = 0):
        self.nom = nom
        self.solde = solde
        
    def __str__(self):
        return f"Propriétaire : {self.nom}|Solde : {self.solde} €"
    
    def deposer(self,montant):
        self.solde += montant
    
    def retirer(self, montant):
        if montant > self.solde:
           print(f"impossible de retirer {montant}€")
        else:
            self.solde -= montant
            print(f"retrait reussis !")
    

def menu():
    print (f"1. Déposer\n2. Retirer\n3. Afficher le solde\n4. Quitter")

user = Compte(input("entrez votre nom : "))

while True : 
    menu()
    try:
        choix = int(input())
    except:
        print("invalide")
        
    if choix == 1:
        user.deposer(float(input("Combien voulez vous deposer : ")))
        
    elif choix == 2:
        user.retirer(float(input("Combien voulez vous retirer : ")))
    
    elif choix == 3:
        print(user)
    
    elif choix == 4:
        break