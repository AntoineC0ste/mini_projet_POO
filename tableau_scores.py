import json
from os.path import exists

class TableauScores():
    '''Un tableau des scores stocké dans un fichier'''

    def __init__(self, nom_fichier:str):
        self.nom_fichier = nom_fichier
        self.__tabscore = []

        if exists(f"./tableau_scores/{self.nom_fichier}.json"):
            self.charger()


    def sauvegarder(self, nom_joueur:str, new_score:int):
        '''
        Sauvegarde un nouveau score dans le tableau.

        Paramètres
        -------
        nom_joueur = `str` le nom du joueur

        new_score = `int` le score du joueur
        '''
        self.charger()
        self.__tabscore.append([new_score, nom_joueur])
        with open(f"./tableau_scores/{self.nom_fichier}.json", "w") as f:
            json.dump(self.__tabscore, f)
            f.close()

    def charger(self):
        with open(f"./tableau_scores/{self.nom_fichier}.json", 'r') as f:
            self.__tabscore = json.load(f)
            f.close()
    
    def retirer(self, score:tuple[str, int]):
        '''Retire un score du tableau.'''
        self.charger()
        self.__tabscore.remove(score)
        with open(f"./tableau_scores/{self.nom_fichier}.json", "w") as f:
            json.dump(self.__tabscore, f)
            f.close()
    
    def get_tableau(self):
        output = []
        tabscore = self.__tabscore
        score_actuel = [0, "NULL"]
        index_actuel = 0
        for score in range(len(self.__tabscore)):
            for i in range(len(tabscore)):
                if tabscore[i][0] > score_actuel[0]:
                    score_actuel = tabscore[i]
                    index_actuel = i
            output.append(self.__tabscore[index_actuel])
            tabscore.remove(score_actuel)
            index_actuel = 0
            score_actuel = [0, "NULL"]
        return output

    

if __name__ == '__main__':
    tab = TableauScores('tests')
    # tab.charger()
    # tab.sauvegarder("them", 290)
    print(tab.get_tableau())