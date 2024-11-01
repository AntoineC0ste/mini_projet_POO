from game import Game
from menu import Menu
from bouton import Bouton
from texte import Texte
import pygame

pygame.init()

RESOLUTION = (638, 320)
ELITE = ("font/elite.ttf",18)

jeu = Game(resolution= RESOLUTION, 
           difficulte= 0, 
           nbr_balles= 15, 
           fond= pygame.image.load('img/fond.jpg'))

lancer_jeu = Bouton(texte=Texte("Lancer le jeu", ELITE, (0,0,0),(255, 150)), 
                    taille=(250,50), 
                    couleur=(255,255,255), 
                    pos=(200, 100), 
                    redirect=jeu)

tableau_scores = Menu(resolution=RESOLUTION,
                      composantes=[Texte("test", ELITE, (0,0,0), (0,0))],
                      fond='img/fond.jpg')

lancer_tabscore = Bouton(texte=Texte("Tableau de scores", ELITE, (0,0,0),(255, 150)),
                         pos=(200, 200),
                         taille=(250,50),
                         couleur=pygame.Color(255,255,255),
                         redirect=tableau_scores)

menu_principal = Menu(resolution=RESOLUTION,
                      composantes=[lancer_jeu, lancer_tabscore],
                      fond='img/fond.jpg')

menu_principal.run()