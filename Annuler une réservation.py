# Annuler une réservation
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
