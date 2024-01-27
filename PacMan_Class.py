import pygame
import csv


# Création de la class PacMan:
class PacMan:
    def __init__(self, sizeX: int, sizeY: int, filename: str, color: pygame.Color):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.filename = filename
        self.color = color
        self.matrice = []

    def ReadFile(self):
        """Lecteur de fichier CSV"""
        with open(self.filename, newline = '') as csvfile:
            loopreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
            for row in loopreader:
                row_list = [int(cell) for cell in row]
                self.matrice.append(row_list)
    
    def DrawMap(self, screen, tilesize):
        """Fonction de dessin de la map"""
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] == 1:
                    pygame.draw.rect(screen, self.color, pygame.Rect(j * tilesize, i * tilesize, tilesize, tilesize))

    def PrintMap(self):
        """Affiche la map"""
        for row in self.matrice:
            print(row)

    def GetMatrice(self):
        return self.matrice
    
    def GetXY(self, i, j):
        return self.matrice[j][i]

    def SetXY(self, i, j, v):
        self.matrice[j][i] = v

    def GetSize(self):
        return self.sizeX, self.sizeY

    def BreakWall(self, i, j):
        self.matrice[j][i] = 0