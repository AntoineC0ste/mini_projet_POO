import pygame
from tableau_scores import TableauScores
from random import random, uniform
from balle import Balle
from menu import Menu
from texte import Texte
class Game():
    '''La fenêtre de jeu principale'''
    def __init__(self, resolution:tuple[int], difficulte:int, nbr_balles:int, fond:pygame.Surface, tabscore:TableauScores, ips=60, redirect = None):
        self.screen = pygame.display.set_mode((resolution[0], resolution[1]))
        self.difficulte = difficulte
        self.fond = fond
        self.clock = pygame.time.Clock()
        self.ips = ips
        self.running = False
        self.balles = [Balle(random()*resolution[0]-55, random()*resolution[1]-55, vitesse=(difficulte+1)*2, taille=uniform(1/(difficulte+1), 1)) for i in range(nbr_balles)]
        self.score = 0
        self.liste_click = []
        self.redirect = redirect
        self.tabscore = tabscore
        pygame.mixer.music.load('sons/qwak.mp3')

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
                    pygame.mixer.music.play()
                    self.balles.remove(balle)
                    self.liste_click.append(1)
                    cooldown = True
            if event.type == pygame.MOUSEBUTTONDOWN and not cooldown and self.score > 0:
                self.liste_click.append(0)

                

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
            self.afficher_texte(f"Score: {int(self.score*100)}%", ("font/elite.ttf", 18), pygame.Color(255,255,255), (0,300))
            
            if self.balles == []:
                self.end()

            pygame.display.update()
            self.clock.tick(self.ips)

    def end(self):
        '''Met fin au jeu'''
        if self.redirect is not None:
            self.tabscore.sauvegarder("MEGABALLULTRAPLACEHOLDERNOONEISGOINGTOECRIRECA", self.score*100)
            self.redirect.run()
            self.running = False
        else:
            self.running = False

if __name__ == "__main__":
    print("-------TESTS-------")
    pygame.init()
    game = Game(resolution=(638, 320),
                difficulte=2,
                nbr_balles=5,
                fond=pygame.image.load('img/fond.jpg'))
    game.run()