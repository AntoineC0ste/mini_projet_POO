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
        self.fond = fond
        self.clock = pygame.time.Clock()
        self.ips = ips
        self.running = True
        self.balles = [Balle(random()*resolution[0]-55, random()*resolution[1]-55) for i in range(nbr_balles)]
        self.score = 0
        self.liste_click = []

    def afficher_balles(self):
        '''Met à jour la position des balles et les affiche à l'écran'''
        for balle in self.balles:
            balle.update()
            balle.est_au_bord(self.screen)
            self.screen.blit(balle.image, (balle.get_x(), balle.get_y()))
    
    def afficher_texte(self, p_contenu:str, p_police:tuple[str,int], p_couleur:pygame.Color, p_pos:tuple[float]):
        texte = Texte(p_contenu, p_police, p_couleur, p_pos)
        self.screen.blit(texte.police, texte.pos)

    def boucle_event(self):
        '''Boucle d'évènements. Permet la détection des entrées du joueur'''
        for event in pygame.event.get():
            cooldown = False
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.running = False
            
            for balle in self.balles:
                if balle.est_touche() and event.type == pygame.MOUSEBUTTONDOWN and not cooldown:
                    self.balles.remove(balle)
                    self.liste_click.append(1)
                    cooldown = True
                if not balle.est_touche() and event.type == pygame.MOUSEBUTTONDOWN and not cooldown and self.score > 0:
                    self.liste_click.append(0)
                    cooldown = True
                

    def run(self):
        '''Boucle principale du jeu'''
        while self.running:
            self.screen.blit(self.fond, (0, 0))

            self.boucle_event()
            self.afficher_balles()

            if self.liste_click != []:
                self.score = sum(self.liste_click)/len(self.liste_click)
                self.score = round(self.score, 2)

            self.afficher_texte("Projet NSI", ("font/elite.ttf", 16), pygame.Color(255,255,255), (490, 300))
            self.afficher_texte(f"Score: {int(self.score*100)}%", ("font/elite.ttf", 18), pygame.Color(255,255,255), (0,0))
            
            if self.balles == []:
                self.end()

            pygame.display.update()
            self.clock.tick(self.ips)

    def end(self):
        '''Met fin au jeu'''
        self.running = False