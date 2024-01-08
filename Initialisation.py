# Module Initialisation contient les fonctions qui permettent d'initialiser une partie
# avec des paramètres par défaut ou automatiques

from Types import TData, TJoueur, TGrilleMat
from EntreesSorties import initialisationManueleJoueur, initialisationManueleJoueurIA, saisirTailleMat


# La fonction initialisation crée et initialise les entitées nécéssaires au fonctionnement du jeu
# si le parametre jeuRapide = True alors on initialise la partie avec des attributs par défauts
# la fonction retourne la structure de donnée data
def initialisation(jeuRapide: bool) -> TData:
    nouvelleData: TData = TData()
    if jeuRapide:
        nouvelleData.append(initialiserTGrilleMat(0, 0))
        nouvelleData.append(initialiserJoueur(False))
        nouvelleData.append(initialiserJoueurIA(False))
        nouvelleData.append(True)
        return nouvelleData
    else:
        lignesEtColonnes = saisirTailleMat()
        nouvelleData.append(initialiserTGrilleMat(lignesEtColonnes[0], lignesEtColonnes[1]))
        nouvelleData.append(initialiserJoueur(True))
        nouvelleData.append(initialiserJoueurIA(True))
        nouvelleData.append(True)
        return nouvelleData


# renvoi un type TGrilleMat initialisé en fonction du nb de lignes et colonnes passés en parametre
# si les 2 valent 0 alors la grille est initialisée en 8*8
def initialiserTGrilleMat(nbLignes: int, nbColonnes: int) -> TGrilleMat:
    res: TGrilleMat = []
    if (nbLignes & nbColonnes) != 0:
        for i in range(nbLignes):
            res.append(['.' for _ in range(nbColonnes)])
        return res
    else:
        for i in range(8):
            res.append(['.' for _ in range(8)])
        return res


# initialise un joueur , possibilité de saisir les  valeurs à l'initialisation
def initialiserJoueur(saisieManuel: bool) -> TJoueur:
    res: TJoueur = []
    if saisieManuel:  # cas ou on demande manuelement à l'utilisateur si il veut un coup sepcial et son pion
        listInfoJoueur: list[bool, str] = initialisationManueleJoueur()
        res.append(listInfoJoueur[0])
        res.append(listInfoJoueur[1])
        res.append(0)
        return res
    else:
        res.append(True)
        res.append('o')
        res.append(0)
        return res


# initialise un joueurIa , possibilité dTe saisir les  valeurs à l'initialisation
def initialiserJoueurIA(saisieManuel: bool) -> TJoueur:
    res: TJoueur = []
    if saisieManuel:  # cas ou on demande manuelement à l'utilisateur si il veut que l'ia ait un coup sepcial et
        # son pion
        listInfoJoueurIa: list[bool, str, int] = initialisationManueleJoueurIA()
        res.append(listInfoJoueurIa[0])
        res.append(listInfoJoueurIa[1])
        res.append(listInfoJoueurIa[2])
        return res
    else:
        res.append(True)
        res.append('x')
        res.append(1)
        return res
