import pygame
import random
import math

class Balle():
    '''Crée une balle.'''
    def __init__(self, x:float, y:float, taille:float=1):
        self.__pos = {"x":x, "y":y}
        self.taille = taille
        angle = 2*math.pi*random()
        self.dx = 5*math.cos(angle)
        self.dy = 5*math.sin(angle)
    
    def update(self):
        self.__pos["y"], self.__pos["x"] += self.dx, self.dy

    def est_au_bord(self, screen:pygame.display) -> bool:
        '''Vérifie si la balle est au bord de l'écran. \n
        Renvoie `True` si la balle est sur un bord de l'écran, `False` sinon.'''

        boundaries = screen.get_window_size() # Renvoie le tuple qui représente la taille de l'écran.
        if (self.__pos["x"] > boundaries[0]-50 and self.dx>0) or (boundaries[0] < 0 and self.dx < 0):
            return True
        elif (self.__pos["y"] > boundaries[1]-50 and self.dy>0) or (boundaries[1] < 0 and self.dy < 0):
            return True
        else: 
            return False
    
    def get_x(self):
        '''Retourne la valeur de la position en x de la balle. \n 
        Retourne: x=:class:`float`'''

        return self.__pos["x"]
    def get_y(self): 
        '''Retourne la valeur de la position en y de la balle. \n 
        Retourne: y=:class:`float`'''
        return self.__pos["y"]
    
    def set_postion(self, x:float, y:float):
        '''met à jour la position de la balle selon les paramètres spécifiés.'''
        self.__pos = {"x":x, "y":y}