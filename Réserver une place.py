# Réserver une place
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