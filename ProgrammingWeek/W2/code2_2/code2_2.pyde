x = 100
def setup():
    size(500,500)
    
def draw_balloon(x,y):
    ellipse(x,y,50,50)
    line(x,y+25,x,y+100)

def draw():
    global x
    draw_balloon(x,200)
    x = x + 10
    if x > 500:
        x = 0
