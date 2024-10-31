from game import Game
from menu import Menu
from bouton import Bouton
from texte import Texte
import pygame

pygame.init()

jeu = Game(resolution= (638, 320), 
           difficulte= 0, 
           nbr_balles= 15, 
           fond= pygame.image.load('img/fond.jpg'))

lancer_jeu = Bouton(texte=Texte("Lancer le jeu", ("font/elite.ttf",18), (0,0,0),(255, 150)), 
                    taille=(250,50), 
                    couleur=(255,255,255), 
                    pos=(200, 100), 
                    redirect=jeu)

menu_principal = Menu(resolution=(638,320),
                      composantes=[lancer_jeu],
                      fond='img/fond.jpg')

menu_principal.run()