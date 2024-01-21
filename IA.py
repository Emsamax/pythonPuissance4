"""
    @file IA.py
    @brief Le module IA contient les algo du fonctionnement de l'IA
"""

import math
import random
from typing import List, Any, Type, Tuple

from Types import *
from Verification import *
from Jouer import jouer, testColonnePleine, creerCoup, placerPion
from random import randint
import copy


def testIAPoserPion(data: TData):
    colonne = randint(0, 7)
    # tant que la colonne n'est pas valide on demande une autre valeur de la colonne
    while testColonnePleine(data[0], colonne):
        colonne = randint(0, 7)
    res = jouer(data, colonne)
    return colonne, res


def minMax(data: TData, profondeur: int, joueur: TJoueur, coupPrecedent: TCoup, lesCoups: list[TCoup]) -> tuple[
    float, TCoup, list[TCoup]]:
    """
    @brief Algorithme Min-Max pour déterminer le coup optimal pour l'IA.

    @param data: Les données du jeu.
    @param profondeur: La profondeur de recherche.
    @param joueur: Le joueur actuel (IA).
    @param coupPrecedent: Le dernier coup joué.
    @param lesCoups: Liste pour enregistrer tous les coups simulés.
    @return: Un tuple avec le score du coup optimal, le dernier coup joué, et la liste de tous les coups simulés.
    """
    # === declaration des variables ===

    meilleurScore: float = -10000.0
    pireScore: float = 100000.0

    # recupere le joueur ia
    joueurIA: TJoueur = avoirJoueur(data, True)
    pionIA: str = joueurIA[1]
    # recupere le joueur non ia
    joueurNonIA: TJoueur = avoirJoueur(data, False)
    pionNonIA: str = joueurNonIA[1]

    # recupere la grille et son nombre de colonnes
    grille: TGrilleMat = data[0]
    nbColonnes: int = len(grille[0])

    #  la profondeur = 0 fin de la recursivité, on retourne la liste de coups lesCoups  qui contient tous les coups du chemin optimal
    # on retourne aussi le score du coup
    if profondeur == 0:
        return evaluationCoup(data, pionIA, pionIA), coupPrecedent, lesCoups

    # === dans la partie recursive de l'algo minMax ===

    # declaration d'une variable de type TCoup à vide
    coupSimule: TCoup = []
    # score du coup actuel
    valeur: float = 0.0

    if joueur == joueurIA:
        # dans minmax partie joueur IA
        # on boucle sur les colonnes
        for i in range(nbColonnes):
            # si la colonne n'est pas pleine
            if not testColonnePleine(data[0], i):
                # simulation d'un coup de l'ia dans la colonne i
                # resDataSimule est un tuple [Tdata, Tcoup]
                resDataSimule = genererTdata(data, i, False)
                # affectation des valeurs de retour da fonction genererTdata dans des variables
                dataSimule: TData = resDataSimule[0]
                coupPrecedent = resDataSimule[1]
                # si le coup simule n'est pas null
                if dataSimule is not None:
                    # instruction recursive
                    resultatMinMax = minMax(dataSimule, profondeur - 1, joueurNonIA, coupPrecedent, lesCoups)
                    if isinstance(resultatMinMax, tuple) and meilleurScore < resultatMinMax[0]:
                        # on recupere le max score du minmax suivant
                        valeur = max(meilleurScore, resultatMinMax[0])
                        coupSimule = copy.deepcopy(resultatMinMax[1])
                        # ajout du coup simule à la liste de coups joués
                        lesCoups.append(coupSimule)
        # cas ou il n'y a plus de place dans la colonne
    else:
        # dans la partie recursive ou on simule les coups que le joueur peut faire
        # boucle sur le nombre de colonnes dans la grille
        for i in range(nbColonnes):
            # teste si la colonne n'est pas pleine
            if not testColonnePleine(data[0], i):
                # on simule le coup que le joueur pourrait faire dans la colonne i
                resDataSimule = genererTdata(data, i, True)
                print(resDataSimule, "simulation pour la colonne i : ", i)
                if resDataSimule is not None:
                    dataSimule: TData = resDataSimule[0]
                    coupPrecedent = resDataSimule[1]
                    # instruction recursive
                    resultatMinMax = minMax(dataSimule, profondeur - 1, joueurIA, coupPrecedent, lesCoups)
                    # si le score que l'on obtient avec le minmax <= pire score pire score on prend le min des deux
                    if isinstance(resultatMinMax, tuple) and pireScore > resultatMinMax[0]:
                        valeur = min(pireScore, resultatMinMax[0])
                        print("nouveau min trouve :", valeur, "colonne ", i)
                        coupSimule = copy.deepcopy(resultatMinMax[1])
                        # on copie le coup simulé et on l'enregistre dans la liste les coups
                        lesCoups.append(coupSimule)
            # cas ou il n'y a plus de place dans la colonne

    # return float, TCoup, TData renvoi la valeur du coup optimal, la data dans lequel ce coup à été simulé la liste de tous les coups joués
    return evaluationCoup(data, pionIA, pionNonIA), coupSimule, lesCoups



def evaluationCoup(data: TData, pionJoueur: str, pionAdversaire: str) -> float:
    """
      @brief attribue un score entre -1 et 1 (compris)
      le score est fait à partir d'une moyenne ponderee avec le nombre de suite de 2 pions contigus que l'ia posède
      et le nombre de suite de 3 pions contigus que lia posedde
      une suite de 3 compte pour 3 dans la moyenne ponderee et une suite de 2 compte pour 2
      si il y n  suites de 3 alors elles conteront comme 3*n dans la moyenne ponderee

      @param data : toutes les informations de ce jeu
      @param pionJoueur : le string qui représente le pion du joueur
      @param pionIa : le string qui représente le pion de l'ia
      @return le score de la Tdata passé en parametre
      """
    seq2Joueur: int = compterSequences(data[0], 2, pionJoueur)
    seq3Joueur: int = compterSequences(data[0], 3, pionJoueur)
    seq2Adversaire: int = compterSequences(data[0], 2, pionAdversaire)
    seq3Adversaire: int = compterSequences(data[0], 3, pionAdversaire)
    return normaliser_score(seq2Joueur + (3 * seq3Joueur) + seq2Adversaire + (3 * seq3Adversaire) / 2)


def normalisation(x: float) -> float:
    """
       @brief noramlise un nombre sur l'interval 0, 1 compris

       @param x qui est le nombre à normaliser
       @return le nombre normalisé sur l'intervalle [0, 1]
       """
    return 1 / (1 + math.exp(-x))


def normaliser_score(score)-> float:
    """
     @brief projette un intervalle de valeur entre [0, 1] sur l'intervalle [-1,  1]

     @param score qui est le score normalisé entre [0, 1]  à projeter sur [-1, 1]
     @return le score normalisé
     """
    normalized_score: float = normalisation(score)
    final_score: float = 2 * normalized_score - 1
    return final_score


from Types import TGrilleMat, TCoup
def compterSequences(grille: TGrilleMat, longueurSequence: int, joueur: str) -> int:
    """
    @brief compte les sequence de n pions dans une grille

    @param grille qui est la grille de jeu
    @param longueurSequence
    @param joueur : le string qui repesente un joueur
    @return le nombre de sequence de n pions présentes dans la grille
    """
    n = len(grille)
    nbSequences = 0

    # En ligne
    for i in range(n):
        for j in range(n - longueurSequence + 1):
            if all(grille[i][j + k] == joueur for k in range(longueurSequence)):
                nbSequences += 1

    # En colonne
    for j in range(n):
        for i in range(n - longueurSequence + 1):
            if all(grille[i + k][j] == joueur for k in range(longueurSequence)):
                nbSequences += 1

    # Diagonale principale
    for i in range(n - longueurSequence + 1):
        for j in range(n - longueurSequence + 1):
            if all(grille[i + k][j + k] == joueur for k in range(longueurSequence)):
                nbSequences += 1

    # Diagonale secondaire
    for i in range(n - longueurSequence + 1):
        for j in range(longueurSequence - 1, n):
            if all(grille[i + k][j - k] == joueur for k in range(longueurSequence)):
                nbSequences += 1

    return nbSequences



def genererTdata(data: TData, nbClonnes: int, joueurNONIa: bool) -> tuple[TData, TCoup] | None:
    """
    @brief genere une Tdata avec un coup joué dans une colonne ou ne fait rien si la colonne est pleine

    @param nbColonnes la colonne dans laquelle sera placé le pion
    @param joueurNONIa booleen qui précise sous quel joueur on doit generer un coup
    @return tuple qui contient la data et le coup simulé OU rien
    """
    if joueurNONIa:
        joueur: TJoueur = data[1]
        if not testColonnePleine(data[0], nbClonnes):
            #copie de la data avec copy.deepcopy pour avoir une nouvelle instance de ce type
            cpyData: TData = copy.deepcopy(data)
            #creation du coup avec la copie de la data et la colonne précisée
            coupSimulation: TCoup = creerCoup(cpyData, joueur, nbClonnes)
            dataSimule: TData = placerPion(cpyData, coupSimulation)
            return dataSimule, coupSimulation
        else:
            return None
    else:
        joueur: TJoueur = data[2]
        if not testColonnePleine(data[0], nbClonnes):
            # copie de la data avec copy.deepcopy pour avoir une nouvelle instance de ce type
            cpyData: TData = copy.deepcopy(data)
            # creation du coup avec la copie de la data et la colonne précisée
            coupSimulation: TCoup = creerCoup(cpyData, joueur, nbClonnes)
            dataSimule: TData = placerPion(cpyData, coupSimulation)
            return dataSimule, coupSimulation
        else:
            return None


def avoirJoueur(data: TData, joueurIA: bool) -> TJoueur:
    """
      @brief retourne un des 2 joueurs présents dans la data

      @param data
      @param joueurIA booleen indique si c'est le joueurIA qui sera retourné ou non
      """
    if joueurIA:
        return data[2]
    else:
        return data[1]
