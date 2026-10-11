class Balloon(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        line(self.x, self.y, self.x, self.y + 100)
        ellipse(self.x, self.y, self.r, self.r)

    def move(self):
        if self.y > height / 2:
            self.y = self.y - 2
        else:
            self.y = self.y - 4
        if self.y < -100:
            self.y = height + 50

balloons = []

def setup():
    size(600, 600)
    x_coords = [100, 200, 300, 400, 500]
    y_coords = [550, 500, 600, 450, 580]
    i = 0
    while i < len(x_coords):
        balloons.append(Balloon(x_coords[i], y_coords[i], random(40, 70)))
        i = i + 1

def draw():
    background(255)
    fill(255, 100, 100)
    i = 0
    while i < len(balloons):
        balloons[i].show()
        balloons[i].move()
        i = i + 1
