from tetromino import Tetromino

class Opiece(Tetromino):
    def __init__(self, coords, color, held):
        super().__init__(coords, color, held)

    def resetCoords(self):
        self.coords = [[0,4],[0,5],[1,4],[1,5]]

    def rotate(self, amount):
        if amount:
            return