# Afficher la liste des passagers d’un train donné.

trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set(["Kenan", "Gregoire"])},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 0, 'passagers': set(["Alex", "Timéo", "Aurian"])},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}

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
