"""
@file: Initialisation.py
@brief  Initialisation : Module Initialisation contient les fonctions qui permettent d'initialiser une partie
avec des paramètres par défaut ou automatiques
"""
from Types import TData, TJoueur, TGrilleMat
from EntreesSorties import initialisationManueleJoueur, initialisationManueleJoueurIA, saisirTailleMat


def initialisation(jeuRapide: bool) -> TData:
    """
       @brief Crée et initialise les entités nécessaires au fonctionnement du jeu.

       Si le paramètre jeuRapide est True, alors initialise la partie avec des attributs par défaut.
       La fonction retourne la structure de donnée data.

       @param jeuRapide: Indique si l'initialisation doit se faire en mode rapide.
       @return: La structure de données initialisée.
       """
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


def initialiserTGrilleMat(nbLignes: int, nbColonnes: int) -> TGrilleMat:
    """
       @brief Renvoie un type TGrilleMat initialisé en fonction du nombre de lignes et colonnes passées en paramètre.

       Si les deux valeurs sont 0, alors la grille est initialisée en 8x8.

       @param nbLignes: Le nombre de lignes de la grille.
       @param nbColonnes: Le nombre de colonnes de la grille.
       @return: La grille initialisée.
       """
    res: TGrilleMat = []
    if (nbLignes & nbColonnes) != 0:
        for i in range(nbLignes):
            res.append(['.' for _ in range(nbColonnes)])
        return res
    else:
        for i in range(8):
            res.append(['.' for _ in range(8)])
        return res


def initialiserJoueur(saisieManuel: bool) -> TJoueur:
    """
       @brief Initialise un joueur, possibilité de saisir les valeurs à l'initialisation.

       @param saisieManuel: Indique si la saisie doit se faire manuellement.
       @return: Le joueur initialisé.
       """
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


def initialiserJoueurIA(saisieManuel: bool) -> TJoueur:
    """
        @brief Initialise un joueur IA, possibilité de saisir les valeurs à l'initialisation.

        @param saisieManuel: Indique si la saisie doit se faire manuellement.
        @return: Le joueur IA initialisé.
    """
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
