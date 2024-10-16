import pygame
import math
from random import random
from balle import Balle

class Game():
    '''La fenêtre de jeu principale'''
    def __init__(self, resolution:tuple[int], difficulte:int, nbr_balles:int, fond:pygame.Surface, ips=60):
        self.screen = pygame.display.set_mode((resolution[0], resolution[1]))
        self.difficulte = difficulte
        # self.nbr_balles = nbr_balles
        self.fond = fond
        self.clock = pygame.time.Clock()
        self.ips = ips
        self.running = True
        self.balles = [Balle(random()*resolution[0]-55, random()*resolution[1]-55) for i in range(nbr_balles)]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.running = False

            self.screen.blit(self.fond, (0, 0))

            for balle in self.balles:
                balle.update()
                balle.est_au_bord(self.screen)
                self.screen.blit(balle.image, (balle.get_x(), balle.get_y()))

            pygame.display.update()
            self.clock.tick(self.ips)