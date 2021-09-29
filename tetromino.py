class Tetromino:
    def __init__(self, coords, color, held):
        self.coords = coords
        self.color = color
        self.held = held

    def been_held(self):
        return self.held
        
    def move_left(self):
        for i in range(len(self.coords)):
            self.coords[i][1] -= 1

    def move_right(self):
        for i in range(len(self.coords)):
            self.coords[i][1] += 1

    def move_down(self):
        for i in range(len(self.coords)):
            self.coords[i][0] += 1

    def move_up(self):
        for i in range(len(self.coords)):
            self.coords[i][0] -= 1

    def rotate(self, amount):
        pass

    