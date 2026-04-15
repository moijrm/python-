def message():
    return "1. Ajouter tâche\n2. Voir tâche\n3. Supprimer tâche\n4.quitter\n"

tache = []
numero = 0

while True:
    print(message())
    try:
        choix = int(input("entrer votre choix (1,2,3,4) : "))
    
    
        if choix == 1:
            ecrire = input("Que voulez vous ajoutez : ")
            tache.append(ecrire)
        elif choix == 2:
            for t in tache:
                numero = numero +1
                print(f"{numero}.{t}")
            print()
        elif choix == 3:
            del tache[int(input("faites votre choix : "))]
        elif choix == 4:
            break
    except :
        print("Valeur invalide")
        