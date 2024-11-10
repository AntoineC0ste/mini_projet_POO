import pygame
import random
import math

class Balle():
    '''
    Crée une balle.

    Attributs:
    -------
    x = :class:`float` qui représente la position initiale de la balle en abscisse 

    y = :class:`float` qui représente la position initiale de la balle en ordonnée

    vitesse = :class:`int` est le multiplicateur de vitesse

    taille = :class:`Optional:float` représente la taille de la balle
    '''
    def __init__(self, x:float, y:float, vitesse:int, taille:float=1):
        self.__pos = {"x":x, "y":y}
        # self.taille = abs(taille)
        angle = 2*math.pi*random.random()
        self.dx = vitesse*math.cos(angle)
        self.dy = vitesse*math.sin(angle)
        self.image = pygame.image.load('img/balle.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (abs(taille), abs(taille)))
    
    def update(self):
        '''Met la postion de la balle à jour en fonction de ses attributs de vitesse'''
        self.__pos["y"] += self.dy
        self.__pos["x"] += self.dx

    def est_au_bord(self, screen:pygame.display) -> bool:
        '''Vérifie si la balle est au bord de l'écran. \n
        Renvoie `True` si la balle est sur un bord de l'écran, `False` sinon.'''

        boundaries = screen.get_size() # Renvoie le tuple qui représente la taille de l'écran.
        if (self.__pos["x"] > boundaries[0]-50 and self.dx>0) or (self.get_x() < 0 and self.dx < 0):
            self.dx = -self.dx
        elif (self.__pos["y"] > boundaries[1]-50 and self.dy>0) or (self.get_y() < 0 and self.dy < 0):
            self.dy = -self.dy
    
    def get_x(self):
        '''Retourne la valeur de la position en x de la balle. \n 
        Retourne: x=:class:`float`'''
        return self.__pos["x"]

    def get_y(self): 
        '''Retourne la valeur de la position en y de la balle. \n 
        Retourne: y=:class:`float`'''
        return self.__pos["y"]
    
    def set_postion(self, x:float, y:float):
        '''Met à jour la position de la balle selon les paramètres spécifiés.'''
        self.__pos = {"x":x, "y":y}

    def est_touche(self) -> bool:
        '''Détecte si le curseur de la souris est sur la balle. \n
        Renvoie `True` si le curseur se trouve sur la balle, `False` sinon.'''
        return self.image.get_rect(topleft=(self.__pos['x'], self.__pos['y'])).collidepoint(pygame.mouse.get_pos())
