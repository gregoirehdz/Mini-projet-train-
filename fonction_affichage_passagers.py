# Afficher la liste des passagers d’un train donné.

def afficher_passager(trains):
    trajet = input("Quelle est le trajet ? : ").strip().upper()

    if trajet not in trains:
        print("Ce trajet n'existe pas")
        return

    passagers = sorted(trains[trajet]["passagers"])

    if not passagers :
        print("Il n'y a aucun passager.")
    else :
        print (f"Il y a {trajet}")
        for p in passagers:
            print("-",p)

afficher_passager(trains)
