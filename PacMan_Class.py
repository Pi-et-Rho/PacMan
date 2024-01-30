import pygame
import csv
import random


# Création de la class PacMan:
class PacMan:
    def __init__(self, sizeX: int, sizeY: int, filename: str, color: pygame.Color):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.size = (sizeX, sizeY)
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
        return self.size

    def BreakWall(self, i, j):
        self.matrice[j][i] = 0

class Ghost:
    def __init__(self, spawn):
        self.position = pygame.Vector2(spawn)
        self.speed = 100

    def move_random(self, size, map_matrice):
        direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        new_position = self.position.copy()

        if direction == "UP":
            new_position.y -= 1
        elif direction == "DOWN":
            new_position.y += 1
        elif direction == "LEFT":
            new_position.x -= 1
        elif direction == "RIGHT":
            new_position.x += 1
        
        if 0 <= new_position.x < size[0] and 0 <= new_position.y < size[1] and map_matrice[int(new_position.y)][int(new_position.x)] != 1:
            self.position = new_position