#  Programme de gestion de trains


# Structure de départ
trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}


# 1 Afficher les trains
def afficher_trajets(trains):
    print("\n LISTE DES TRAJETS ")
    for trajet, info in trains.items():
        print(f"{trajet} → {info['places_restantes']} places restantes / {info['places_total']}")


# 2 Réserver une place
def reserver_place(trains):
    nom = input("Nom du passager : ").strip()
    trajet = input("Code du trajet : ").strip().upper()

    if trajet not in trains:
        print("Ce trajet n'existe pas.")
        return

    info = trains[trajet]

    if info['places_restantes'] == 0:
        print("Ce train est complet.")
        return

    if nom in info['passagers']:
        print("Ce passager a déjà une réservation.")
        return

    # Réservation
    info['passagers'].add(nom)
    info['places_restantes'] -= 1

    # BONUS : génération de ticket (tuple)
    numero_place = info['places_total'] - info['places_restantes']
    ticket = (nom, trajet, numero_place)

    print(f"Réservation confirmée pour {nom} sur {trajet}.")
    print(f"Ticket : {ticket}")


# 3 Annuler une réservation
def annuler_reservation(trains):
    nom = input("Nom du passager : ").strip()
    trajet = input("Code du trajet : ").strip().upper()

    if trajet not in trains:
        print("Trajet inconnu.")
        return

    info = trains[trajet]

    if nom not in info['passagers']:
        print("Ce passager n'a pas de réservation sur ce trajet.")
        return

    info['passagers'].remove(nom)
    info['places_restantes'] += 1

    print(f"Réservation de {nom} annulée pour {trajet}.")


# 4 Afficher les passagers d’un train
def afficher_passagers(trains):
    trajet = input("Code du trajet : ").strip().upper()

    if trajet not in trains:
        print("Trajet inconnu.")
        return

    passagers = sorted(trains[trajet]['passagers'])

    print(f"\nPassagers du trajet {trajet} :")
    if not passagers:
        print("Aucun passager pour ce trajet.")
    else:
        for p in passagers:
            print(" -", p)


# 5 Afficher les trains complets
def afficher_trains_complets(trains):
    print("\n TRAINS COMPLETS")
    complets = [t for t, info in trains.items() if info['places_restantes'] == 0]

    if not complets:
        print("Aucun train n'est complet.")
    else:
        for t in complets:
            print("🚆", t)


#  Menu principal


def menu():
    while True:
        print("\n MENU RÉSERVATION TRAIN ")
        print("1  Afficher les trains")
        print("2  Réserver une place")
        print("3  Annuler une réservation")
        print("4  Afficher les passagers d’un train")
        print("5  Voir les trains complets")
        print("0  Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            afficher_trajets(trains)
        elif choix == "2":
            reserver_place(trains)
        elif choix == "3":
            annuler_reservation(trains)
        elif choix == "4":
            afficher_passagers(trains)
        elif choix == "5":
            afficher_trains_complets(trains)
        elif choix == "0":
            print("Au revoir ")
            break
        else:
            print(" Choix invalide, veuillez réessayer.")


# Lancement du programme
menu()
