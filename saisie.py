from bouton import Bouton
from texte import Texte
from tableau_scores import TableauScores
import pygame

class Saisie(Bouton):
    '''Crée un rectangle pour la saisie de texte par l'utilisateur

    Paramètres
    -------

    position = :class:`tuple[float]` les coordonnées du texte saisi dans un couple **(x,y)**

    taille = :class:`tuple[float]` la taille du texte saisi dans un couple **(longueur, largeur)**

    couleur_bg = :class:`pygame.Color()` la valeur RGB de la couleur de l'arrière plan du texte saisi, peut aussi être **(R, G, B)**

    couleur_txt = :class:`pygame.Color()` la valeur RGB de la couleur du texte saisi, peut aussi être **(R, G, B)**
    '''
    
    def __init__(self, position:tuple[float], taille:tuple[float], couleur_bg:pygame.Color, couleur_txt:pygame.Color):
        super().__init__(texte=Texte("", ("font/elite.ttf",18), couleur_txt,(255, 150)),
                       pos=position,
                       taille=taille,
                       couleur=couleur_bg,
                       redirect=None)
    
    def update(self, screen:pygame.Surface, event:pygame.event=None, tabscore:TableauScores=None):
        '''Affiche le champ de saisie sur la surface spécifiée et gère l'entrée utilisateur'''
        if event != None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.texte.set_contenu(self.texte.get_contenu()[:-1])
                elif event.key == pygame.K_RETURN:
                    self.change_score(tabscore)
                    self.current_app.end()
                else:
                    self.texte.set_contenu(self.texte.get_contenu()+event.unicode)

        screen.blit(self.surf, self.pos)
        screen.blit(self.texte.police, self.surf.get_rect(topleft=self.pos).midleft)
    
    def change_score(self, tabscore:TableauScores):
        '''Remplace un score vide avec le pseudo saisi'''
        for score in tabscore.get_tableau():
            if score[1] == "MEGABALLULTRAPLACEHOLDERNOONEISGOINGTOECRIRECA":
                num = score[0]
                tabscore.retirer(score)
                tabscore.sauvegarder(self.texte.get_contenu(), num)
                break





if __name__ == "__main__":
    pygame.init()
    saisie = Saisie((0,0), (100, 50), (255,255,255), (0,0,0))
    screen = pygame.display.set_mode((256, 256))
    tabscore = TableauScores("tests")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            saisie.update(screen, event, tabscore)
        pygame.display.flip()
        clock.tick(60)
