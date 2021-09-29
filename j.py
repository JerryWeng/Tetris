from tetromino import Tetromino

class Jpiece(Tetromino):
    def __init__(self, coords, color, held):
        super().__init__(coords, color, held)

    def resetCoords(self):
        self.coords = [[0,5],[1,5],[1,4],[1,3]]

    def rotate(self, amount):
        if amount == 1:
            self.coords[0][0] += 1
            self.coords[1][1] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 2
            self.coords[3][1] += 1
        elif amount == 2:
            self.coords[0][1] -= 1
            self.coords[1][0] -= 1
            self.coords[2][1] += 1
            self.coords[3][0] += 1
            self.coords[3][1] += 2
        elif amount == 3:
            self.coords[0][0] -= 1
            self.coords[1][1] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 2
            self.coords[3][1] -= 1
        else:
            self.coords[0][1] += 1
            self.coords[1][0] += 1
            self.coords[2][1] -= 1
            self.coords[3][0] -= 1
            self.coords[3][1] -= 2

        colend1, colend2 = self.coords[0][1], self.coords[3][1]
        rowend1, rowend2 = self.coords[0][0], self.coords[3][0]
        maxc, minc, maxr, minr = 0,0,0,0

        if colend1 > colend2:
            maxc = colend1
            minc = colend2
        elif colend1 < colend2:
            maxc = colend2
            minc = colend1
        if rowend1 > rowend2:
            maxr = rowend1
            minr = rowend2
        elif rowend1 < rowend2:
            maxr = rowend2
            minr = rowend1

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