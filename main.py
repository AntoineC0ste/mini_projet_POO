from game import Game
from menu import Menu
from bouton import Bouton
from saisie import Saisie
from texte import Texte
from tableau_scores import TableauScores

import pygame

pygame.init()
pygame.mixer.init()

RESOLUTION = (638, 320)
ELITE = ("font/elite.ttf",18)

def generer_texte_defaut(texte:str):
    return Texte(texte, ELITE, (0,0,0), (0,0))

tabscore = TableauScores("scores")

saisie_pseudo = Menu(resolution=RESOLUTION,
                     composantes=[Saisie(position=(200,150), taille=(250, 50), couleur_bg=(255, 255, 255), couleur_txt=(0, 0, 0))],
                     fond="img/fond.jpg",
                     tabscore=tabscore)

facile = Game(resolution= RESOLUTION, 
           difficulte= 0, 
           nbr_balles= 15, 
           fond= pygame.image.load('img/fond.jpg'),
           redirect=saisie_pseudo,
           tabscore=tabscore)

lancer_facile = Bouton(texte=generer_texte_defaut("Facile"),
                       pos=(200,50),
                       taille=(250, 50),
                       couleur=(255,255,255),
                       redirect=facile)

moyen = Game(resolution= RESOLUTION, 
             difficulte= 1, 
             nbr_balles= 30, 
             fond= pygame.image.load('img/fond.jpg'),
             redirect=saisie_pseudo,
             tabscore=tabscore)

moyen.running = False # En enlevant cette ligne, le jeu ne se ferme pas et lance la difficulté moyen à la place. NE PAS TOUCHER

lancer_moyen = Bouton(texte=generer_texte_defaut("Moyen"),
                       pos=(200,150),
                       taille=(250, 50),
                       couleur=(255,255,255),
                       redirect=moyen)

difficile = Game(resolution= RESOLUTION, 
                 difficulte= 2, 
                 nbr_balles= 50, 
                 fond= pygame.image.load('img/fond.jpg'),
                 redirect=saisie_pseudo,
                 tabscore=tabscore)

lancer_difficile = Bouton(texte=generer_texte_defaut("Difficile"),
                       pos=(200,250),
                       taille=(250, 50),
                       couleur=(255,255,255),
                       redirect=difficile)

select_difficulte = Menu(resolution=RESOLUTION,
                         composantes=[lancer_facile, lancer_moyen, lancer_difficile],
                         fond='img/fond.jpg')

lancer_jeu = Bouton(texte=Texte("Lancer le jeu", ELITE, (0,0,0),(255, 150)), 
                    taille=(250,50), 
                    couleur=(255,255,255), 
                    pos=(200, 100), 
                    redirect=select_difficulte)

listscore = tabscore.get_tableau() # Pour les itérables en dessous
menu_tableau_scores = Menu(resolution=RESOLUTION,
                      composantes=[Texte(f"{listscore[i][1]}: {int(listscore[i][0])}", ELITE, (0,0,0), (RESOLUTION[0]/2.5,i*25)) for i in range(len(listscore))],
                      fond='img/fond.jpg')

lancer_tabscore = Bouton(texte=Texte("Tableau de scores", ELITE, (0,0,0),(255, 150)),
                         pos=(200, 200),
                         taille=(250,50),
                         couleur=pygame.Color(255,255,255),
                         redirect=menu_tableau_scores)

menu_principal = Menu(resolution=RESOLUTION,
                      composantes=[lancer_jeu, lancer_tabscore],
                      fond='img/fond.jpg')

lancer_menu_principal = Bouton(texte=Texte("Revenir au menu principal", ELITE, (0,0,0),(255, 150)),
                               pos=(630, 300),
                               taille=(80, 35),
                               couleur=(255,255,255),
                               redirect=menu_principal)

saisie_pseudo.parent = menu_principal

menu_principal.run()