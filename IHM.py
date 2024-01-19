"""! @brief Programme IHM
 @mainpage Page IHM du puissance 4
 @section Description programme IHM
 Interface utilisateur du puissance 4, l'interface se compose de
 deux sections :
   - Une partie paramètre
   - Une partie jeu

 La partie paramètre permet de modifer les valeurs par défauts du jeu,
 comme la couleur du pion du joueur (jaune ou rouge) ; la taille de la grille et le niveau de l'IA

 La partie jeu permet d'afficher la grille au cours du jeu, de lancer le jeu et de jouer son atout.

 @section Section importation
 Ce programme utilise les modules ci-dessous:
 from Initialisation import *
 import tkinter as tk
 from tkinter import messagebox
 from tkinter import ttk
 from PIL import ImageTk, Image
 import os
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os
import time
from Jouer import jouer, data, coupSpecial
from IA import testIAPoserPion
from Initialisation import initialiserTGrilleMat

# Fenêtre Tkinter
window = tk.Tk()

# liste des 3 tailles différentes de jeu
listeTaille = ["8x8", "8x7", "9x8"]

# - Grille -#
# Liste des labels de la grille qui contient les images des pions
listeLabelGrille = []

# ! Variable à modifier car init dans le fichier initialisation.py et son contenu dans des "structures"
# => il faudra importer la "structure" et se sera cet "structure" qui sera modifié
# Taille de la grille nbLigne x nbColonne
nbLigne = len(data[0])
nbColonne = len(data[0][0])

# !

# - Variable de jeu -#
# Booléen, Si False => le jeu n'est pas lancé,
# Sinon Si True => le jeu est lancé
jeu = False
# Frame de la grille de jeu contenant, initialisé dans la fonction jeuInit
# - Les boutons pour poser
# - Les labels avec les pions
frameJeu = None

# Atout variable
atoutActive = False

# Liste des images des pions
here = os.getcwd()
imgPions = [
    Image.open(os.path.join(os.path.dirname(__file__),  "img/pion_jaune.jpeg")),
    Image.open(os.path.join(os.path.dirname(__file__),  "img/pion_rouge.png")),
    Image.open(os.path.join(os.path.dirname(__file__),  "img/pion_blanc.png"))
]


# --------------------------------------------------#
# (Ajouter les menus avec Undo / Redo)
def initIHM():
    """
    Fonction qui initialise l'interface
    1. initMenu : Initialise le menu, on passe la fenêtre tkinter en argument
    2. Initialisation des varaibles stringVar, utiliser dans les labels de la section paramètre et section Jeu -> Atout
       Et utilisé pour leurs valeurs : la taille de la grille ; couleurs ; niveau de diffilculté
    3. parametre : Initialisation de la section paramètres
    4. jeuInit : Initialisation
    5. On utilise la méthode mainloop pour démarer l'interface
    :return:
    """
    # Initialise un objet Tkinter
    global window
    # Configuration
    window.title("Puissance 4")
    window.geometry("960x624")

    # Initialise le menu
    initMenu(window)

    # String Variable
    # Pour Partie Paramètre
    tailleGrille = tk.StringVar(window, "8x8")
    couleurChoix = tk.StringVar(window)
    couleurChoix.set("o")  # initialiser
    niveauChoix = tk.StringVar(window)
    niveauChoix.set("1")  # initialiser

    # Partie Grille / jeu
    tour = tk.StringVar(window, "Joueur 1")
    atoutNb = tk.StringVar(window, "1")

    # Initialise la partie paramètre de l'interface
    parametre(window, tailleGrille, couleurChoix, niveauChoix, tour, atoutNb)

    # Initialise la partie jeu avec la grille / les boutons de jeux (atout, lancer une partie)
    jeuInit(window, tour, atoutNb)

    # Affichage Interface
    window.mainloop()


def initMenu(self):
    menubar = tk.Menu(self)

    undoMenu = tk.Menu(menubar, tearoff=0)
    undoMenu.add_command(label="Undo", command=undo)
    menubar.add_cascade(label="Undo", menu=undoMenu)

    redoMenu = tk.Menu(menubar, tearoff=0)
    redoMenu.add_command(label="Redo", command=redo)
    menubar.add_cascade(label="Redo", menu=redoMenu)

    ExitMenu = tk.Menu(menubar, tearoff=0)
    ExitMenu.add_command(label="Quitter", command=self.quit)
    menubar.add_cascade(label="Quitter", menu=ExitMenu)

    self.config(menu=menubar)


def parametre(self, tailleGrille, couleurChoix, niveauChoix, tour, atoutNb):
    frame1 = tk.Frame(self, width=262, height=525, bg="#D9D9D9")
    frame1.pack_propagate(False)
    frame1.pack(side='left', padx=20)

    # Title
    title = tk.Label(frame1, text="Paramètres", fg='black', bg="#D9D9D9", font="TkDefaultFont 28 underline")
    title.pack(padx=10, pady=10)

    # Taille Grille
    # Pour changement de la taille de la grille (label + input)
    tailleLabel = tk.Label(frame1, text="Taile de la grille", bg="#D9D9D9")
    # ComboBox (bouton déroulant)
    listeTailleGrille = ttk.Combobox(frame1, values=listeTaille, state="readonly")
    # Pack
    tailleLabel.pack(padx=10, pady=(10, 0))
    listeTailleGrille.pack(padx=10, pady=2)
    # Element par défaut : 7x6
    listeTailleGrille.current(0)
    # Relie une action au combobox
    # Permet d'ajouter dans la varaible tailleGrille la valeur du combobox
    listeTailleGrille.bind("<<ComboboxSelected>>", lambda e: tailleGrille.set(listeTailleGrille.get()))

    # Niveau de jeu
    couleurLabel = tk.Label(frame1, text="Couleur du joueur :", fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    couleurLabel.pack(anchor='w', padx=(20, 0), pady=(20, 10))
    # Radio bouton (couleur : rouge ou jaune)
    # (Ajouter les commandes plus tard de changement de couleur)
    jauneBtn = tk.Radiobutton(frame1, text="Jaune", variable=couleurChoix, value="o", bg="#D9D9D9")
    rougeBtn = tk.Radiobutton(frame1, text="Rouge", variable=couleurChoix, value="x", bg="#D9D9D9")
    # Pack
    jauneBtn.pack(anchor='w', padx=(60, 0))
    rougeBtn.pack(anchor='w', padx=(60, 0))

    # Niveau IA choix
    niveauLabel = tk.Label(frame1, text="Niveau de l'ordinateur", fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    niveauLabel.pack(anchor='w', padx=(20, 0), pady=(20, 10))
    # Radio bouton (Niveau de jeu : 1 / 2 / 3)
    # (Ajouter les commandes plus tard de changement de couleur)
    niveauBtn1 = tk.Radiobutton(frame1, text="Niveau 1", variable=niveauChoix, value="1", bg="#D9D9D9")
    niveauBtn2 = tk.Radiobutton(frame1, text="Niveau 2", variable=niveauChoix, value="2", bg="#D9D9D9")
    niveauBtn3 = tk.Radiobutton(frame1, text="Niveau 3", variable=niveauChoix, value="3", bg="#D9D9D9")
    # Pack
    niveauBtn1.pack(anchor='w', padx=(60, 0))
    niveauBtn2.pack(anchor='w', padx=(60, 0))
    niveauBtn3.pack(anchor='w', padx=(60, 0))

    # Bouton validation
    # (Ajouter commande de validation des paramètre)
    btnvalidation = tk.Button(frame1, text="Valider",
                              bg="#D9D9D9", highlightthickness=1, highlightbackground="#D9D9D9",
                              font="TkDefaultFont 16",
                              command=lambda: validationParametre(tailleGrille, couleurChoix, niveauChoix))
    btnvalidation.pack(side='bottom', padx=10, pady=(0, 40))


def jeuInit(self, tour, atoutNb):
    global frameJeu

    frame2 = tk.Frame(self, width=650, height=600, bg="#D9D9D9")
    frame2.pack_propagate(False)
    frame2.pack(side='right', padx=20)

    # Label Tour du Joueur (joueur ou IA)
    tourJoueurLabel = tk.Label(frame2, textvariable=tour, fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    tourJoueurLabel.pack(side='top', anchor='nw', padx=(20, 0), pady=(20, 10))

    # Frame grille de jeu
    frameJeu = tk.Frame(frame2, width=375, height=375, bg="#000")
    frameJeu.pack_propagate(False)
    frameJeu.pack(padx=20)

    # Init de la grille
    initGrille()

    # Bouton Jeu / Ajout
    # (Ajouter commande de validation des paramètre)
    btnJeu = tk.Button(frame2, text="Joueur", bg="#D9D9D9",
                       highlightthickness=1, highlightbackground="#D9D9D9", font="TkDefaultFont 16", command=jouerCmd)
    btnJeu.pack(side='left', padx=10, pady=20)
    btnAtout = tk.Button(frame2, text="Jouer Atout",
                         bg="#D9D9D9", highlightthickness=1, highlightbackground="#D9D9D9",
                         font="TkDefaultFont 16", command=lambda: jouerAtout(atoutNb))
    btnAtout.pack(side='left', padx=10, pady=20)
    btnAnnulerAtout = tk.Button(frame2, text="Annuler Atout",
                                bg="#D9D9D9", highlightthickness=1, highlightbackground="#D9D9D9",
                                font="TkDefaultFont 16", command=lambda: AnunulerJouerAtout(atoutNb))
    btnAnnulerAtout.pack(side='left', padx=10, pady=20)

    # Label nombre d'atout
    atoutTextLabel = tk.Label(frame2, text="Nombre d'atout", fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    atoutLabel = tk.Label(frame2, textvariable=atoutNb, fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    atoutTextLabel.pack(side='left', padx=(10, 1), pady=20)
    atoutLabel.pack(side='left', padx=(1, 10), pady=20)


# À Faire
def initGrille():
    # frameGrille : taille 375x375
    # On récupère le nombre de ligne et de colonne
    # On les converti en nombre (int)
    global nbLigne  # = int(tailleGrille.get()[0])
    global nbColonne  # = int(tailleGrille.get()[2])
    global frameJeu

    newSize = (int(375 / nbColonne), int(375 / nbLigne))

    # Import l'image des pions vide
    # Utilisation de la librairie PIL pour pouvoir utiliser les images avec tkinter
    # Met un objet Image (de la librairie PIL) dans la variable image (ouvre l'image)
    image = Image.open("/Users/carineraffin-peyloz/Desktop/informatique/3A/pythonPuissance4/img/pion_blanc.png")
    # On redimensionne l'image selon le nombre de colonne et de ligne
    image = image.resize(newSize)
    # On crée un objet ImageTk compatible avec tkinter pour l'affichage
    img = ImageTk.PhotoImage(image)

    for j in range(nbColonne):
        # frameGrille.grid_columnconfigure(j, weight=2)
        # Création du btn pour chaque colone
        # On affecte une action : poserPion, qui prend en paramètre la colonne du bouton
        # ce qui permettra de poser le pion dans la bonne colonne
        # On utilise la méthode grid pour placer les boutons dans la colonne correspondante
        tk.Button(frameJeu, text="\/", bg="#D9D9D9",
                  highlightthickness=1, highlightbackground="#000", font="TkDefaultFont 10",
                  command=lambda colonne=j: poserPion(colonne)).grid(column=j, row=0)
        listLabel = []
        for i in range(nbLigne):
            label = tk.Label(frameJeu, image=img)
            label.grid(column=j, row=i + 1)
            label.image = img
            listLabel.append(label)
        listeLabelGrille.append(listLabel)


def deleteFrameGrille():
    """
    Fonction qui vide la frame de la grille :
     - supprime les boutons pour poser les pions
     - supprimes les labels
    """
    global frameJeu
    for widget in frameJeu.winfo_children():
        widget.grid_forget()


# - Commande / action des boutons de la frame des paramètres -#
def validationParametre(tailleGrille, couleurChoix, niveauChoix):
    """
    Fonction qui valide les paramètres et mets à jour les variables
     - taille de grille
     - couleur du pion du joueur
     - niveau de l'IA
    :return: none
    """
    # Il faut changer la grille de data si changement de nbLigne et nbColonne
    global listeLabelGrille
    global nbLigne
    global nbColonne
    global jeu

    # Met à jour les paramètres du jeu si le jeux n'est pas lancé
    if not jeu:
        # - Mise à jour valeur de jeu -#
        # On met à jour les variables nbLigne x nbColonne
        nbLigne = int(tailleGrille.get()[0])
        nbColonne = int(tailleGrille.get()[2])
        data[0] = initialiserTGrilleMat(nbLigne, nbColonne)

        # On met à jour la varaible couleur du joueur
        couleur = str(couleurChoix.get())
        # Si 'o' alors le joueur joue avec les jaunes et l'ia avec les rouges (cas par défaut)
        if couleur == 'o':
            data[1][1] = 'o'
            data[2][1] = 'x'
        # Sinon la couleur du joueur est rouge ('x') et l'ia avec les jaunes ('o')
        else:
            data[1][1] = 'x'
            data[2][1] = 'o'

        # On met à jour le niveau de jeu de l'IA
        data[2][2] = int(niveauChoix.get())

        # - Partie réinitialisation Grille -#
        # Vide listeLabelGrille
        listeLabelGrille = []
        # Vide la frame de la grille
        deleteFrameGrille()
        # Réinitialise la frame de la grille avec les bonnes dimensions
        initGrille()

    else:
        messagebox.showinfo("Message du jeu", "Vous ne pouvez pas modifier les paramètres du jeu pendant une partie")



# - Commande des boutons de la frame de Jeu -#
def jouerCmd():
    """
    Fonction qui lance le jeu lorsque le joueur appuie sur le btn jouer
    :return:
    """
    global jeu
    if not jeu:
        jeu = True
        messagebox.showinfo("Message du jeu", "Que le meilleur gagne !!")



def jouerAtout(atoutNb):
    """
    Fonction qui permet d'activé l'atout (jouer l'atout)
    Ne peut être activé que si le nombre d'atout est différent de 0
    :return:
    """
    global jeu
    global atoutActive

    if jeu:
        if atoutNb.get() == "1":
            # L'atout est activé
            atoutActive = True
            # Met le nombre d'atout à 0
            atoutNb.set("0")
        else:
            messagebox.showinfo("Message du jeu", "Vous n'avez plus d'atout")
    else:
        messagebox.showinfo("Message du jeu", "Lancer le jeu pour jouer votre atout")


def AnunulerJouerAtout(atoutNb):
    """
    Fonction qui permet d'annuler l'utilisation de l'atout
    Ne peut être activé que si le nombre d'atout est de 1 (différent de 0)
    Et si la fonction jouerAtout a été exécuté
    :return:
    """
    global atoutActive

    # Si l'atout est activé alors on le désactive sinon c'est qu'il n'est pas activé
    if atoutActive:
        # Annuler l'atout
        atoutActive = False
        atoutNb.set("1")


# -- Action des boutons de jeux de pions sur la grille --#

def changerPionCouleur(colonne, couleur, ligne):
    # Appel des variable global
    global listeLabelGrille
    global nbLigne
    global nbColonne
    global imgPions

    # Définir la taille de la grille
    newSize = (int(375 / nbColonne), int(375 / nbLigne))
    # Vazribale 'j' et 'r' à modifier ?
    if couleur == 'o':
        # Ouvre l'image du pion jaune
        image = imgPions[0]
    elif couleur == 'x':
        # Ouvre l'image du pion rouge
        image = imgPions[1]
    else:
        # Utilisable pour un undo
        image = imgPions[2]

    # Redimensionner l'image
    image = image.resize(newSize)
    # On crée un objet ImageTk compatible avec tkinter pour l'affichage
    img = ImageTk.PhotoImage(image)
    # On modifie l'image dans le label
    listeLabelGrille[colonne][ligne].configure(image=img)
    listeLabelGrille[colonne][ligne].image = img


def poserPion(colonne: int):
    # Variable jeu permet de lancer le jeu en appyant sur le boutton jouer
    global jeu
    global atoutActive
    global window
    # Si le jeu est lancé alors on peut poser un pion sinon impossible
    if jeu:
        if atoutActive:
            #On joue le coup spécial (Atout)
            coupSpecial(data, colonne)

            for i in range(len(listeLabelGrille)):
                changerPionCouleur(colonne, '.', i)
            atoutActive = False

        # On joue le coup du joueur
        res = jouer(data, colonne)
        if res != ():
            # On change la couleur du pion
            print("Couleur joueur : ", data[3])
            changerPionCouleur(colonne, data[1][1], res[0])
            # Joueur a gagné ?
            if res[1]:
                jeu = False
                window.update()
                messagebox.showinfo("Message de victoire", "Le Joueur __ a gagné !")

            # Autour de l'IA
            else:
                # Juste tester si l'IA joue dans une colonne pleine
                resIA = testIAPoserPion(data)
                changerPionCouleur(resIA[0], data[2][1], resIA[1][0])
                if resIA[1][1]:
                    jeu = False
                    window.update()
                    messagebox.showinfo("Message de victoire", "L'ordinateur a gagné !")
    else:
        # message d'information : Appuier sur jouer pour lancer le jeu
        messagebox.showinfo("Message du jeu", "Vous devez lancer le jeu pour pouvoir poser un pion")

# - Fonction Undo -#
def undo():
    pass

def redo():
    pass

def fermerFenetre():
    deleteFrameGrille()
    global window
    window.destroy()


if __name__ == "__main__":
    initIHM()
