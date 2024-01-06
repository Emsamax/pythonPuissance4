# Module Initialisation contient les fonctions qui permettent d'initialiser une partie
# avec des paramètres par défaut ou automatiques
# Initialise ensuite les structures grille, joueurs, pion, donees,
from array import array

from typing import NewType, Any, TypeAlias

from EntreesSorties import initData

# Structure de la grille est composée :
# d'une liste ligne qui contient un entier positif repésentant le nb de ligne de la grille
# et une liste colonne qui contient un entier positif repésentant le nb de colonne de la grille

TGrilleMat: TypeAlias = [list[list[str]]]

# Structure d'un joueur qui est définie par :
# un booléen coupSpécial qui permet de savoir si le coup spécial à été utilisé ou non
# un pion qui est un string
TJoueur: TypeAlias = list[bool, chr]

# Structure de l'IA est la même que celle d'un joueur avec en plus son niveau de difficulté
TJoueurIA: TypeAlias = list[bool, chr, int]

# Structure data représente le jeu à l'instant t
# La structure data est représentée pars :
# une grille
# un joueur qui est le joueur qui joue au puissance4
# un booléen j1tour qui inqique si c'est au joueur1 de jouer
bJ1tour: bool = True
TData: TypeAlias = list[TGrilleMat, TJoueur, TJoueurIA, bool]


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
        nouvelleData[3] = True


# demande à l'utilisateur de saisir le nb de lignes et de colonnes de la grille jusqu'a ce que le format de la grille
# soit acceptable: le nombere de lignes et colonnes de doit pas etre inferieur à 0
def saisirTailleMat() -> list[int]:
    res: list[int] = list()
    valide = False
    while not valide:
        entreeNbLignes = input("saisir nb lignes de la grille")
        res[0] = int(entreeNbLignes)
        entreeNbColonnes = input("saisir nb colonnes de la grille")
        res[1] = int(entreeNbColonnes)
        if (res[0] & res[1] <= 0)():
            print("Erreur : La grille ne peut pas etre sous la forme 0*X ")
        else:
            valide = True
    return res


# renvoi un type TGrilleMat initialisé en fonction du nb de lignes et colonnes passés en parametre
# si les 2 valent 0 alors la grille est initialisée en 8*8
def initialiserTGrilleMat(nbLignes: int, nbColonnes: int) -> TGrilleMat:
    res: TGrilleMat = []
    if (nbLignes & nbColonnes) != 0:
        for i in range(nbLignes):
            res.append(['0' for _ in range(nbColonnes)])
        return res
    else:
        for i in range(8):
            res.append(['.' for _ in range(8)])
        return res


# initialise un joueur , possibilité de saisir les  valeurs à l'initialisation
def initialiserJoueur(saisieManuel: bool) -> TJoueur:
    res: TJoueur = []
    if saisieManuel:  # cas ou on demande manuelement à l'utilisateur si il veut un coup sepcial et son pion
        saisieBool = input("Voulez vous avoir 1 coup special au cours de la partie ? 1 oui 0 sinon")
        res.append(bool(int(saisieBool)))
        saisiePion = input("Saisisez 1 caractere comme pion")
        res.append(saisiePion)
        return res
    else:
        res.append(True)
        res.append('x')
        return res


# initialise un joueurIa , possibilité dTe saisir les  valeurs à l'initialisation
def initialiserJoueurIA(saisieManuel: bool) -> TJoueurIA:
    res: TJoueurIA = []
    if saisieManuel:  # cas ou on demande manuelement à l'utilisateur si il veut que l'ia ait un coup sepcial et
        # son pion
        saisieBool = input("Voulez vous que l'ia ait 1 coup special au cours de la partie ? 1 oui 0 sinon")
        res.append(bool(int(saisieBool)))
        saisiePion = input("Saisisez 1 caractere comme pion pour l'ia")
        res.append(saisiePion)
        saisieDifficulte = input("Saisisez saisisez le niveau de difficulté")
        res.append(int(saisieDifficulte))
        return res
    else:
        res.append(True)
        res.append('x')
        res.append(1)
        return res


def afficherEtatJeu(data: TData) -> None:
    print("[ grille : \n")
    for ligne in data[0]:
        for colonne in ligne:
            print(colonne, end=" ")
        print("`\n")
    print("Joueur : " + str(data[1]))
    print("JoueurIA : " + str(data[2]))
    print("tour du joueur : " + str(data[3]) + "]")
