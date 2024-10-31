import pygame
from texte import Texte

class Bouton():
    '''Crée un bouton cliquable par l'utilisateur'''
    def __init__(self, texte:Texte, taille:tuple[float], couleur:pygame.Color, pos:tuple[float], redirect):
        self.texte = texte
        self.surf = pygame.Surface(taille)
        self.surf.fill(couleur)
        self.surf.get_rect().update(pos, taille)
        self.pos = pos
        self.new_app = redirect
        self.current_app = None


    def est_touche(self) -> bool:
        '''Détecte si le curseur de la souris est sur le bouton. \n
        Renvoie `True` si le curseur se trouve sur le bouton, `False` sinon.'''
        return self.surf.get_rect(topleft=self.pos).collidepoint(pygame.mouse.get_pos())
    
    def update(self, screen:pygame.Surface):
        self.surf.get_rect().update(self.pos, self.surf.get_size())
        screen.blit(self.surf, self.pos)
        screen.blit(self.texte.police, self.surf.get_rect(topleft=self.pos).center)

    def lancer_app(self):
        '''Lance un Menu ou un Game'''
        self.current_app.end()
        self.new_app.run()