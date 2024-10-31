from bouton import Bouton
import pygame

class Menu():
    '''Affiche un menu et ses composantes'''
    def __init__(self, resolution:tuple[int], composantes:list[Bouton], fond:str):
        self.screen = pygame.display.set_mode(resolution)
        self.composantes = composantes
        self.fond = pygame.image.load(fond)
        self.running = True
        self.clock = pygame.time.Clock()
    
    def update_composantes(self, screen:pygame.surface, click:bool):
        for composant in self.composantes:
            composant.update(screen)
            if composant.est_touche() and click:
                composant.action()
            
    def run(self):
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