import pygame
from pygame.font import Font

class Texte():
    '''
    Un élément de texte.

    Attributs:
    ------
    
    contenu = :class:`str` -> le texte à afficher

    police = :class:`tuple` -> ("chemin_vers_la_police", taille:`int`) 

    couleur = :class:`pygame.Color` -> (R,G,B)

    position = :class:`tuple` -> (x:`float`, y:`float`)
    '''
    def __init__(self, contenu:str, police:tuple, couleur:pygame.Color, position:tuple):
        self.__contenu = contenu
        self.police = Font(police[0], police[1]).render(contenu, True, couleur)
        self.couleur = couleur
        self.pos = position


    def get_contenu(self) -> str:
        '''Renvoie le contenu du texte.'''
        return self.__contenu
    
    def set_contenu(self, nouveau_contenu:str) -> None:
        '''Met à jour le texte affiché.'''
        self.__contenu = nouveau_contenu
        self.police = self.police.render(self.__contenu, True, self.couleur)