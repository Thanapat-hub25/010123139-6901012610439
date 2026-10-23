def draw_stairs(x, y, s, n):
    i = 0
    while i < n:
        line(x, y, x + s, y)
        line(x + s, y, x + s, y - s)
        x = x + s
        y = y - s
        i = i + 1

def setup():
    size(500, 500)

def draw():
    background(255)

    n = int(mouseX / 50.0)
    if n < 1:
        n = 1

    stroke(0)
    strokeWeight(3)
    draw_stairs(50, 450, 40, n)
