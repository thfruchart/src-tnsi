#Sujet 4 Epreuve Pratique 2026

corr_E = {'nom' : 'CORR','prenom':'Edouard','nb_personne':4,
                       'duree_sejour':12,'tarif_journalier':30}


# Question 1
def montant_a_regler(client):
    """ renvoie le montant en euros
    à régler pour cette réservation d’un client au format dictionnaire"""
    pass

# Question 2 et 3
calendrier = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
    'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

def separe(chaine):
    """renvoie une liste constituée de chaînes qui étaient
    séparées par le caractère - """
    return chaine.split('-')

def que_des_chiffres(chaine):
    """renvoie vrai si chaine n'est constituée que
    des caractères de 0 à 9 faux sinon"""
    for car in chaine:
        if not(car in "012345789"):
            return False
    return True

def facture_est_valide(chaine):
    """renvoie vrai si chaine est une chaîne de
    caractères conforme au modèle de facture"""
    partie = separe(chaine)
    if not(len(partie) == 3):
        return False
    annee, mois, numero = partie[0], partie[1], partie[2]
    if not(que_des_chiffres(annee)):
        return False
    if not(len(annee) == 4) or not(2018 <= annee <= 2024):
        return False
    # Reste à faire vérifier les mois MMM
    pass
    # Reste à faire vérifier le numéro xxx *
    pass
    return True

"""
#Exemple d'utilisation de la fonction split
texte = 'Bonjour-le-monde'
separateur = '-'
resultat = texte.split(separateur)
print(resultat)
"""


# Question 4
#assert ..., "  "


#Question 5
def chiffre_affaire(liste):
    """ renvoie la somme des montants de la liste des factures en euros, passée en paramètre
    les factures non valides ne doivent pas être prises en compte dans le calcul de la somme.
    la liste de facture est une liste de dictionnaire.
    """
    pass

liste_facture = [ {'numero' : '2024-MAY-230', 'montant' : 145},
                    {'numero' : '2012-MAY-230', 'montant' : 230},
                    {'numero' : '2024-AMI-231', 'montant' : 55},
                    {'numero' : '2024-JUN-23', 'montant' : 16},
                    {'numero' : '2024-JUN-241', 'montant' : 10}]


#assert chiffre_affaire(liste_facture) ...



