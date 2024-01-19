# Le module IA contient les algo du fonctionnement de l'IA
# Le module utilise une structure coup en interne.

from Verification import *
from Jouer import jouer, data, testColonnePleine
from random import randint

def testIAPoserPion(data: TData):
    colonne = randint(0, 7)
    # tant que la colonne n'est pas valide on demande une autre valeur de la colonne
    while testColonnePleine(data[0], colonne):
        colonne = randint(0, 7)
    res = jouer(data, colonne)
    return colonne, res