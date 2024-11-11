from bouton import Bouton
from saisie import Saisie
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

    tabscore = :class:`Optionnal:TableauScores` pour le menu de saisie de pseudo
    '''
    def __init__(self, resolution:tuple[int], composantes:list[Bouton], fond:str, tabscore=None):
        self.screen = pygame.display.set_mode(resolution)
        self.composantes = composantes
        self.fond = pygame.image.load(fond)
        self.running = True
        self.clock = pygame.time.Clock()
        self.parent = None
        self.tabscore = tabscore
        for composant in self.composantes:
            if isinstance(composant, Bouton):
                composant.current_app = self
    
    def update_composantes(self, screen:pygame.Surface, click:bool, event:pygame.event=None, tabscore=None):
        '''Affiche et teste l'état des composantes
        Paramètres
        -------
        screen = :class:`pygame.Surface` la surface sur laquelle afficher les composantes

        click = :class:`bool` représente si un clic est détécté pour l'activation des boutons

        event = :class:`Optional:pygame.event` l'evènement pygame pour détecter l'entrée du clavier
        '''
        for composant in self.composantes:
            if isinstance(composant, Texte):
                screen.blit(composant.police, composant.pos)

            elif isinstance(composant, Bouton):
                if isinstance(composant, Saisie) and event != None:
                    composant.update(screen, event, tabscore)
                elif event == None:
                    composant.update(screen)
                    if composant.est_touche() and click:
                        composant.lancer_app(self)

            
    def run(self):
        '''Boucle principale du menu'''
        while self.running:
            self.screen.blit((self.fond), (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and self.parent != None:
                    self.parent.running = True
                    self.parent.run()
                    self.end()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.update_composantes(self.screen, True)
                self.update_composantes(self.screen, False, event, self.tabscore)

        
            self.update_composantes(self.screen, False)
            pygame.display.update()
            self.clock.tick(30)

    def end(self):
        '''Ferme le menu'''
        self.running = False