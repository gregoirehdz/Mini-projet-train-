# Afficher les trains

def affiche_train(trains):
    for train, info in trains.items():
        places_total = info['places_total']
        places_restantes = info['places_restantes'] 
        print (f"Le trajet {train} avec {places_total} places total et {places_restantes} place disponible")

affiche_train(trains)