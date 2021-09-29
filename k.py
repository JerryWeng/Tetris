from tetromino import Tetromino

class Kpiece(Tetromino):
    def __init__(self, coords, color, held):
        super().__init__(coords, color, held)

    def resetCoords(self):
        self.coords = [[0,4],[1,3],[1,4],[1,5]]

    def rotate(self, amount):
        if amount == 1:
            self.coords[0][0] += 1
            self.coords[0][1] += 1
            self.coords[1][0] -= 1
            self.coords[1][1] += 1
            self.coords[3][0] += 1
            self.coords[3][1] -= 1
        elif amount == 2:
            self.coords[0][0] += 1
            self.coords[0][1] -= 1
            self.coords[1][0] += 1
            self.coords[1][1] += 1
            self.coords[3][0] -= 1
            self.coords[3][1] -= 1
        elif amount == 3:
            self.coords[0][0] -= 1
            self.coords[0][1] -= 1
            self.coords[1][0] += 1
            self.coords[1][1] -= 1
            self.coords[3][0] -= 1
            self.coords[3][1] += 1
        else:
            self.coords[0][0] -= 1
            self.coords[0][1] += 1
            self.coords[1][0] -= 1
            self.coords[1][1] -= 1
            self.coords[3][0] += 1
            self.coords[3][1] += 1

        colends = [self.coords[0][1], self.coords[1][1], self.coords[3][1]]
        rowends = [self.coords[0][0], self.coords[1][0], self.coords[3][0]]
        maxc, minc, maxr, minr = float('-inf'),float('inf'),float('-inf'),float('inf')

        for i in range(len(colends)):
            if colends[i] > maxc:
                maxc = colends[i]
            if colends[i] < minc:
                minc = colends[i]

        for i in range(len(rowends)):
            if rowends[i] > maxr:
                maxr = rowends[i]
            if rowends[i] < minr:
                minr = rowends[i]


        if maxc > 9:
            for i in range(len(self.coords)):
                for _ in range(maxc - 9):
                    self.coords[i][1] -= 1
        elif minc < 0:
            for i in range(len(self.coords)):
                for _ in range(abs(minc)):
                    self.coords[i][1] += 1
        if maxr > 19:
            for i in range(len(self.coords)):
                for _ in range(maxr - 19):
                    self.coords[i][0] -= 1
        elif minr > 19:
            for i in range(len(self.coords)):
                for _ in range(minr - 19):
                    self.coords[i][0] -= 1

                


            
