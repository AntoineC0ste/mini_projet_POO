import pygame
from pygame.font import Font

class Texte():

    def __init__(self, contenu:str, police:tuple, couleur:pygame.Color, position:tuple):
        self.__contenu = contenu
        self.police = Font(police[0], police[1]).render(contenu, True, couleur)
        self.couleur = couleur
        self.pos = position


    def get_contenu(self):
        return self.__contenu
    
    def set_contenu(self, nouveau_contenu):
        self.__contenu = nouveau_contenu
        self.police = self.police.render(self.__contenu, True, self.couleur)