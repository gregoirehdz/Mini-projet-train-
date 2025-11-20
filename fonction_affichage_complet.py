# Afficher les trains complets.

def train_complet(trains):
   for trajet, info in trains.items():
      if info["places_restantes"] == 0:
         print (f"Le trajet {trajet} est complet.")

train_complet(trains)