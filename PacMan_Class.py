import pygame
import csv
import random
import heapq

# Création de la classe PacMan:
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
        with open(self.filename, newline='') as csvfile:
            loopreader = csv.reader(csvfile, delimiter=',', quotechar='|')
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

    def move_random(self, target, size, map_matrice):
        def reconstruct_path(came_from, current):
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.insert(0, current)
            return path

        def get_neighbors(node):
            x, y = node
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            return neighbors

        def distance(node1, node2):
            x1, y1 = node1
            x2, y2 = node2
            return abs(x1 - x2) + abs(y1 - y2)

        # Convertir la position en tuple
        start = (int(self.position.x), int(self.position.y))
        target = (int(target.x), int(target.y))

        open_set = [(0, start)]  # Utilisez une file de priorité pour maintenir les nœuds à explorer
        came_from = {}  # Garde une trace des nœuds précédents pour reconstruire le chemin
        g_score = {start: 0}  # Coût réel pour atteindre chaque nœud

        while open_set:
            current_f, current = heapq.heappop(open_set)

            if current == target:
                # Reconstruire le chemin si le nœud actuel est la cible
                path = reconstruct_path(came_from, current)
                if len(path) > 1:  # Assurez-vous que le chemin a plus d'un nœud
                    return pygame.Vector2(path[1])  # Retourne le prochain nœud dans le chemin (le suivant après la position actuelle)

            for neighbor in get_neighbors(current):
                tentative_g = g_score[current] + 1  # Le coût entre chaque nœud est considéré comme 1 dans une grille

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    # Mettez à jour les informations si la nouvelle route est meilleure
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + distance(neighbor, target)
                    heapq.heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current

        # Si l'open set est vide et la cible n'a pas été atteinte, restez immobile
        return pygame.Vector2(start)