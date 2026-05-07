import csv

def numeros_et_noms(fichier_csv: str) -> dict:
    arrets = {}
    with open(fichier_csv, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arret1_num = int(row['Numéro Arrêt 1'])
            arret1_nom = row['Nom Arrêt 1']
            arret2_num = int(row['Numéro Arrêt 2'])
            arret2_nom = row['Nom Arrêt 2']

            # Ajout des arrêts au dictionnaire
            if arret1_num not in arrets:
                arrets[arret1_num] = arret1_nom
            if arret2_num not in arrets:
                arrets[arret2_num] = arret2_nom

    return arrets

def csv_to_graphe(fichier_csv: str) -> dict:
    graphe = {}

    with open(fichier_csv, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arret1_num = int(row['Numéro Arrêt 1'])
            arret2_num = int(row['Numéro Arrêt 2'])

            # Initialisation des entrées pour chaque arrêt
            if arret1_num not in graphe:
                graphe[arret1_num] = []
            if arret2_num not in graphe:
                graphe[arret2_num] = []

            # Ajout des voisins
            graphe[arret1_num].append({
                'numero': arret2_num,
                'distance': int(row['Distance (minutes)'])
            })
            graphe[arret2_num].append({
                'numero': arret1_num,
                'distance': int(row['Distance (minutes)'])
            })

    return graphe

def plus_court_chemin(graphe, arret_depart, arret_arrivee):
    # Initialisation des distances et des prédécesseurs
    distances = {arret: float('inf') for arret in graphe}
    distances[arret_depart] = 0
    predecesseurs = {arret: None for arret in graphe}

    # Liste des arrêts à visiter
    a_visiter = []
    for arret in graphe:
        a_visiter.append(arret)

    while a_visiter:
        # Trouver l'arrêt avec la plus petite distance non visitée
        arret_actuel = a_visiter[0]
        min_distance = distances[arret_actuel]
        for arret in a_visiter:
            if distances[arret] < min_distance:
                arret_actuel = arret
                min_distance = distances[arret]

        a_visiter.remove(arret_actuel)

        # Si on a atteint l'arrêt d'arrivée, reconstruire le chemin
        if arret_actuel == arret_arrivee:
            chemin = []
            current = arret_actuel
            while current is not None:
                chemin.insert(0, current)  # On ajoute l'arrêt au début de la liste pour obtenir le chemin dans le bon ordre
                current = predecesseurs[current]  # On remonte au prédécesseur
            return (distances[arret_arrivee], chemin)  # Retourne la distance totale et le chemin

        # Mettre à jour les distances des voisins
        for voisin in graphe[arret_actuel]:
            nouvelle_distance = distances[arret_actuel] + voisin['distance']
            if nouvelle_distance < distances[voisin['numero']]:
                distances[voisin['numero']] = nouvelle_distance
                predecesseurs[voisin['numero']] = arret_actuel

    # Si on sort de la boucle sans avoir trouvé l'arrêt d'arrivée, retourner une distance infinie et un chemin vide
    return (float('inf'), [])

    