import pygame
from texte import Texte

class Bouton():
    '''
    Crée un bouton cliquable par l'utilisateur

    Paramètres
    -------

    texte = :class:`Texte` objet texte qui sera affiché sur le bouton

    pos = :class:`tuple[float]` les coordonnées du bouton dans un couple **(x,y)**

    taille = :class:`tuple[float]` la taille du bouton dans un couple **(longueur, largeur)**

    couleur = :class:`pygame.Color()` la valeur RGB de la couleur du bouton, peut aussi être **(R, G, B)**

    redirect = :class:`Menu`/:class:`Game` le menu/jeu lancé par le bouton
    '''

    def __init__(self, texte:Texte, pos:tuple[float], taille:tuple[float], couleur:pygame.Color, redirect):
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
        '''Affiche le bouton sur la surface spécifiée'''
        screen.blit(self.surf, self.pos)
        screen.blit(self.texte.police, self.surf.get_rect(topleft=self.pos).center)

    def lancer_app(self):
        '''Lance un Menu ou un Game, spécifiés à la création du bouton'''
        self.current_app.end()
        self.new_app.run()