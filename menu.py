from bouton import Bouton
from texte import Texte
import pygame

class Menu():
    '''
    Affiche un menu et ses composantes
    
    Paramètres
    ------
    resolution = :class:`tuple[int]` la résoltion de la fenêtre (longueur, hauteur)

    composantes = :class:`list[Bouton, Texte]` liste de composantes du menu

    fond = :class:`str` chemin d'accès vers le fichier du fond d'écran du menu
    '''
    def __init__(self, resolution:tuple[int], composantes:list[Bouton], fond:str):
        self.screen = pygame.display.set_mode(resolution)
        self.composantes = composantes
        self.fond = pygame.image.load(fond)
        self.running = True
        self.clock = pygame.time.Clock()

        for composant in self.composantes:
            if isinstance(composant, Bouton):
                composant.current_app = self
    
    def update_composantes(self, screen:pygame.Surface, click:bool):
        '''Affiche et teste l'état des composantes
        Paramètres
        -------
        screen = :class:`pygame.Surface` la surface sur laquelle afficher les composantes

        click = :class:`bool` représente si un clic est détécté pour l'activation des boutons
        '''
        for composant in self.composantes:
            if isinstance(composant, Texte):
                screen.blit(composant.police, composant.pos)

            elif isinstance(composant, Bouton):
                composant.update(screen)
                if composant.est_touche() and click:
                    composant.lancer_app()
            
    def run(self):
        '''Boucle principale du menu'''
        while self.running:
            self.screen.blit((self.fond), (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.update_composantes(self.screen, True)

        
            self.update_composantes(self.screen, False)
            pygame.display.update()
            self.clock.tick(30)

    def end(self):
        '''Ferme le menu'''
        self.running = False