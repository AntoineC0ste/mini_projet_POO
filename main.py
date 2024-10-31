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

menu_principal = Menu(resolution=(638,320),
                      composantes=[Bouton(Texte("Jeu de bouboules", ("font/elite.ttf",18), (255,255,255), (255, 150)), (250,100), (0,255,255), (0,0))],
                      fond='img/fond.jpg')

# jeu.run()
menu_principal.run()