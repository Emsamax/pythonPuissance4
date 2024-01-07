# Contient tous les types utilisés dans le puissance4 afin d'éviter les dépendances circulaires

# Initialise ensuite les structures grille, joueurs, pion, donees,
from array import array

from typing import TypeAlias

# Structure de la grille est composée :
# d'une liste ligne qui contient un entier positif repésentant le nb de ligne de la grille
# et une liste colonne qui contient un entier positif repésentant le nb de colonne de la grille

TGrilleMat: TypeAlias = [list[list[str]]]

# Structure d'un joueur qui est définie par :
# un booléen coupSpécial qui permet de savoir si le coup spécial à été utilisé ou non
# un pion qui est un string
# un int qui représente le niveau de difficulté  de l'ia, si = 0 alors le joueur n'est pas une ia
TJoueur: TypeAlias = list[bool, str, int]

# Structure data représente le jeu à l'instant t
# La structure data est représentée pars :
# une grille
# un joueur qui est le joueur qui joue au puissance4
# un booléen j1tour qui inqique si c'est au joueur1 de jouer
bJ1tour: bool = True
TData: TypeAlias = list[TGrilleMat, TJoueur, TJoueur, bool]

#liste qui sauvegarde tous les etats du jeu : le dernier coup joué est le dernier element de la liste
TSauvegardeEtatJeu: TypeAlias = list[TData]

# Cet Alias repésente un coup sous la forme : le joueur qui l'a joué, la ligne et la colonne du coup
TCoup: TypeAlias = list[TJoueur, list[1]]
