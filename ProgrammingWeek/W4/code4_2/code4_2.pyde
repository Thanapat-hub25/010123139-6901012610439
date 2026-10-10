def setup():
    size(500, 500)

def draw_cloude(x,y):
    noStroke()
    fill(128, 128, 128)
    ellipse(x, y, 50, 50)
    ellipse(x+50, y, 50, 50)
    ellipse(x+100, y, 50, 50)
    ellipse(x+25, y-20, 50, 50)
    ellipse(x+75, y-20, 50, 50)

def draw_rain(x, y):
    stroke(0, 0, 255)
    strokeWeight(5)
    line(x, y, x, y + 25)

def draw_balloon(x, y):
    fill(255, 0, 0)
    stroke(0)
    strokeWeight(1)
    ellipse(x, y, 100, 100)
    line(x, y + 50 , x, y + 200)

def draw():
    background(255)
    draw_cloude(25,60)
    draw_cloude(200,60)
    draw_cloude(375,60)
    x = random(50, 450)
    y = random(150, 250)
    draw_rain(x, y)
    draw_balloon(250,250 )
