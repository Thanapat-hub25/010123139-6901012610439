def setup():
    size(500,500)
    
def draw_circle(x, y, r):
    ellipse(x,y,r*2,r*2)

def draw_balloon(x,y):
    draw_circle(x,y,50)
    line(x,y+50,x,y+200)
    
def draw():
    background(255)
    #x = random(100,300)
    #y = random(150,250)
    draw_balloon(mouseX,mouseY)
