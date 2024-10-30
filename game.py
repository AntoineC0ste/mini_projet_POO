import pygame
import math
from random import random
from balle import Balle
from texte import Texte
class Game():
    '''La fenêtre de jeu principale'''
    def __init__(self, resolution:tuple[int], difficulte:int, nbr_balles:int, fond:pygame.Surface, ips=60):
        self.screen = pygame.display.set_mode((resolution[0], resolution[1]))
        self.difficulte = difficulte
        self.score = Texte("Projet NSI", ("font/elite.ttf", 16), pygame.Color(255,255,255), (490, 300))
        self.fond = fond
        self.clock = pygame.time.Clock()
        self.ips = ips
        self.running = True
        self.balles = [Balle(random()*resolution[0]-55, random()*resolution[1]-55) for i in range(nbr_balles)]

    def afficher_balles(self):
        '''Met à jour la position des balles et les affiche à l'écran'''
        for balle in self.balles:
            balle.update()
            balle.est_au_bord(self.screen)
            self.screen.blit(balle.image, (balle.get_x(), balle.get_y()))

    def boucle_event(self):
        '''Boucle d'évènements. Permet la détection des entrées du joueur'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.running = False
            
            for balle in self.balles:
                if balle.est_touche() and event.type == pygame.MOUSEBUTTONDOWN:
                    self.balles.remove(balle)

    def run(self):
        '''Boucle principale du jeu'''
        while self.running:
            self.screen.blit(self.fond, (0, 0))

            self.boucle_event()
            self.afficher_balles()

            self.screen.blit(self.score.police, (490,300))

            pygame.display.update()
            self.clock.tick(self.ips)