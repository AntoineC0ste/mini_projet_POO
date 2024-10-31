import pygame
from texte import Texte

class Bouton():
    '''Crée un bouton cliquable par l'utilisateur'''
    def __init__(self, texte:Texte, taille:tuple[float], couleur:pygame.Color, pos:tuple[float]):
        self.texte = texte
        self.surf = pygame.Surface(taille)
        self.surf.fill(couleur)
        self.pos = pos


    def est_touche(self) -> bool:
        '''Détecte si le curseur de la souris est sur le bouton. \n
        Renvoie `True` si le curseur se trouve sur le bouton, `False` sinon.'''
        return self.surf.get_rect().collidepoint(pygame.mouse.get_pos())
    
    def update(self, screen:pygame.Surface):
        screen.blit(self.surf, self.pos)
        screen.blit(self.texte.police, (self.surf.get_rect().left+2*len(self.texte.get_contenu()), self.surf.get_rect().centery))
    
    def action(self):
        print("test")