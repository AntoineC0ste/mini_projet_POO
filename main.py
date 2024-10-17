from game import Game
from balle import Balle
import math
import pygame

pygame.init()

jeu = Game(resolution= (638, 320), 
           difficulte= 0, 
           nbr_balles= 15, 
           fond= pygame.image.load('img/fond.jpg'))

jeu.run()
