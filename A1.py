import math
import random
g = 9.8
v0 = 60.0
angle_deg = 45.0

t = 0.0
is_firing = False
fire_effect = 0

path_x = []
path_y = []

origin_x = 80
origin_y = 390
scale = 4

target_x = 550
target_w = 40
hit_target = False

def setup():
    size(800, 500)
    frameRate(30)

def draw_background():
    background(210, 230, 250)
    
    noStroke()
    fill(180, 200, 220)
    triangle(100, 390, 250, 220, 400, 390)
    fill(160, 185, 210)
    triangle(280, 390, 480, 180, 680, 390)
    
    fill(90, 170, 100)
    rect(0, origin_y, 800, 110)
    fill(120, 195, 120)
    rect(0, origin_y, 800, 10)

def draw_target():
    fill(220, 50, 50)
    stroke(255)
    strokeWeight(2)
    rect(target_x, origin_y - 12, target_w, 12, 3)
    fill(255)
    rect(target_x + 10, origin_y - 12, target_w - 20, 12)
    
    if hit_target:
        fill(230, 50, 50)
        textSize(20)
        text("BULLSEYE! HIT!", target_x - 30, origin_y - 25)

def draw_cannon():
    pushMatrix()
    translate(origin_x, origin_y)
    
    global fire_effect
    if fire_effect > 0:
        fill(255, 200, 50, 200)
        noStroke()
        ellipse(cos(radians(angle_deg)) * 45, -sin(radians(angle_deg)) * 45, 35, 35)
        fill(255, 100, 0, 150)
        ellipse(cos(radians(angle_deg)) * 55, -sin(radians(angle_deg)) * 55, 20, 20)
        fire_effect -= 1

    rotate(radians(-angle_deg))
    fill(60)
    stroke(30)
    strokeWeight(2)
    rect(0, -10, 40, 20, 4)
    fill(40)
    rect(-5, -12, 10, 24, 2)
    popMatrix()
    
    fill(80)
    stroke(40)
    arc(origin_x, origin_y, 36, 36, PI, TWO_PI)

def draw_dotted_preview():
    stroke(120, 140, 160)
    strokeWeight(2)
    rad = math.radians(angle_deg)
    vx = v0 * math.cos(rad)
    vy = v0 * math.sin(rad)
    
    prev_x = origin_x
    prev_y = origin_y

    sim_t = 1
    while sim_t < 25:
        st = sim_t * 0.25
        sx = origin_x + (vx * st * scale)
        sy = origin_y - (((vy * st) - (0.5 * g * (st ** 2))) * scale)
        
        if sy > origin_y:
            break
        if sim_t % 2 == 0:
            line(prev_x, prev_y, sx, sy)
        prev_x = sx
        prev_y = sy
        sim_t += 1

def draw_ui():
    fill(255, 255, 255, 220)
    stroke(200)
    strokeWeight(1)
    rect(15, 12, 770, 65, 12)
    
    fill(40)
    textSize(14)
    text("ANGLE: " + str(int(angle_deg)) + " deg", 35, 42)
    text("SPEED: " + str(int(v0)) + " m/s", 235, 42)
    
    fill(230, 240, 250)
    stroke(150)
    rect(145, 25, 28, 25, 5)
    rect(178, 25, 28, 25, 5)
    
    rect(345, 25, 28, 25, 5)
    rect(378, 25, 28, 25, 5)
    
    fill(0)
    textSize(16)
    text("-", 155, 42)
    text("+", 187, 42)
    text("-", 355, 42)
    text("+", 387, 42)
    
    if is_firing:
        fill(235, 87, 87)
    else:
        fill(46, 204, 113)
    noStroke()
    rect(435, 20, 110, 36, 8)
    
    fill(52, 152, 219)
    rect(560, 20, 140, 36, 8)
    
    fill(255)
    textSize(15)
    if is_firing:
        text("RESET", 465, 43)
    else:
        text("FIRE !", 468, 43)
    text("NEW TARGET", 580, 43)

def draw():
    global t, path_x, path_y, is_firing, hit_target
    
    draw_background()
    draw_target()
    
    if not is_firing:
        draw_dotted_preview()
        
    draw_cannon()
    draw_ui()
    
    noFill()
    stroke(231, 76, 60)
    strokeWeight(3)
    beginShape()
    i = 0
    while i < len(path_x):
        vertex(path_x[i], path_y[i])
        i += 1
    endShape()

    if is_firing:
        rad = math.radians(angle_deg)
        vx = v0 * math.cos(rad)
        vy = v0 * math.sin(rad)
        x_m = vx * t
        y_m = (vy * t) - (0.5 * g * (t ** 2))
        
        screen_x = origin_x + (x_m * scale)
        screen_y = origin_y - (y_m * scale)

        path_x.append(screen_x)
        path_y.append(screen_y)

        fill(40)
        stroke(255, 200, 0)
        strokeWeight(1.5)
        ellipse(screen_x, screen_y, 14, 14)

        if screen_x >= target_x and screen_x <= (target_x + target_w) and screen_y >= (origin_y - 15):
            hit_target = True

        t = t + 0.15

        if screen_y >= origin_y and t > 0.5:
            is_firing = False

def mousePressed():
    global angle_deg, v0, is_firing, t, path_x, path_y, target_x, hit_target, fire_effect
    
    if mouseX >= 145 and mouseX <= 173 and mouseY >= 25 and mouseY <= 50:
        if angle_deg > 10 and not is_firing: 
            angle_deg -= 5
            
    elif mouseX >= 178 and mouseX <= 206 and mouseY >= 25 and mouseY <= 50:
        if angle_deg < 85 and not is_firing: 
            angle_deg += 5
            
    elif mouseX >= 345 and mouseX <= 373 and mouseY >= 25 and mouseY <= 50:
        if v0 > 10 and not is_firing: 
            v0 -= 5
            
    elif mouseX >= 378 and mouseX <= 406 and mouseY >= 25 and mouseY <= 50:
        if v0 < 100 and not is_firing: 
            v0 += 5
            
    elif mouseX >= 435 and mouseX <= 545 and mouseY >= 20 and mouseY <= 56:
        if not is_firing:
            t = 0.0
            path_x = []
            path_y = []
            is_firing = True
            hit_target = False
            fire_effect = 3
        else:
            t = 0.0
            path_x = []
            path_y = []
            is_firing = False
            hit_target = False

    elif mouseX >= 560 and mouseX <= 700 and mouseY >= 20 and mouseY <= 56:
        target_x = int(random.uniform(300, 700))
        hit_target = False