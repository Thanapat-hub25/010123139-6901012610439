x = []
y = []
speed = []

def draw_circle(cx, cy, r):
    ellipse(cx, cy, r, r)

def draw_cloud():
    noStroke()
    fill(150)
    draw_circle(150, 110, 70)
    draw_circle(220, 110, 70)
    draw_circle(290, 110, 70)
    draw_circle(185, 80, 70)
    draw_circle(255, 80, 70)

def draw_vertical_lines(x1, y1, x2, y2):
    space = abs(x1 - x2) / 5.0
    while x1 < x2:
        line(x1, y1 - 50, x1, y1 + 50)
        x1 = x1 + space

def draw_fence():
    stroke(100, 60, 20)
    strokeWeight(4)
    draw_vertical_lines(0, 450, 500, 450)
    line(0, 435, 500, 435)
    line(0, 465, 500, 465)

def setup():
    size(500, 500)
    i = 0
    while i < 10:
        x.append(random(100, 400))
        y.append(random(150, 300))
        speed.append(random(2, 6))
        i = i + 1

def draw():
    background(255)
    draw_cloud()
    draw_fence()

    stroke(0, 0, 255)
    strokeWeight(3)
    i = 0
    while i < len(x):
        line(x[i], y[i], x[i], y[i] + 15)
        y[i] = y[i] + speed[i]
        if y[i] > 400:
            y[i] = random(150, 200)
            x[i] = random(100, 400)
        i = i + 1

def mousePressed():
    x.append(mouseX)
    y.append(mouseY)
    speed.append(random(2, 6))
