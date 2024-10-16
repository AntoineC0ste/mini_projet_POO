from game import Game
from balle import Balle
import math
import pygame

pygame.init()

jeu = Game(resolution= (720, 800), 
           difficulte= 0, 
           nbr_balles= 100, 
           fond= pygame.image.load('img/fond.jpg'))

jeu.run()
