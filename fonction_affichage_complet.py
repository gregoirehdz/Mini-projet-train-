# Afficher les trains complets.

trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set(["Kenan", "Gregoire"])},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 0, 'passagers': set(["Alex", "Timéo", "Aurian"])},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}

def train_complet(trains):
   for trajet, info in trains.items():
      if info["places_restantes"] == 0:
         print (f"Le trajet {trajet} est complet.")

train_complet(trains)