# Afficher les trains
def afficher_trajets(trains):
    print("\n LISTE DES TRAJETS ")
    for trajet, info in trains.items():
        print(f"{trajet} → {info['places_restantes']} places restantes / {info['places_total']}")
