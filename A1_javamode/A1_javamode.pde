float g = 9.8f;
float v0 = 60.0f;
float angleDeg = 45.0f;

float t = 0.0f;
boolean isFiring = false;
int fireEffect = 0;

ArrayList<Float> pathX = new ArrayList<Float>();
ArrayList<Float> pathY = new ArrayList<Float>();

float originX = 80;
float originY = 390;
float scale = 4;

float targetX = 550;
float targetW = 40;
boolean hitTarget = false;

void setup() {
  size(800, 500);
  frameRate(30);
}

void drawBackground() {
  background(210, 230, 250);
  
  noStroke();
  fill(180, 200, 220);
  triangle(100, 390, 250, 220, 400, 390);
  fill(160, 185, 210);
  triangle(280, 390, 480, 180, 680, 390);
  
  fill(90, 170, 100);
  rect(0, originY, 800, 110);
  fill(120, 195, 120);
  rect(0, originY, 800, 10);
}

void drawTarget() {
  fill(220, 50, 50);
  stroke(255);
  strokeWeight(2);
  rect(targetX, originY - 12, targetW, 12, 3);
  fill(255);
  rect(targetX + 10, originY - 12, targetW - 20, 12);
  
  if (hitTarget) {
    fill(230, 50, 50);
    textSize(20);
    text("BULLSEYE! HIT!", targetX - 30, originY - 25);
  }
}

void drawCannon() {
  pushMatrix();
  translate(originX, originY);
  
  if (fireEffect > 0) {
    fill(255, 200, 50, 200);
    noStroke();
    ellipse(cos(radians(angleDeg)) * 45, -sin(radians(angleDeg)) * 45, 35, 35);
    fill(255, 100, 0, 150);
    ellipse(cos(radians(angleDeg)) * 55, -sin(radians(angleDeg)) * 55, 20, 20);
    fireEffect -= 1;
  }

  rotate(radians(-angleDeg));
  fill(60);
  stroke(30);
  strokeWeight(2);
  rect(0, -10, 40, 20, 4);
  fill(40);
  rect(-5, -12, 10, 24, 2);
  popMatrix();
  
  fill(80);
  stroke(40);
  arc(originX, originY, 36, 36, PI, TWO_PI);
}

void drawDottedPreview() {
  stroke(120, 140, 160);
  strokeWeight(2);
  float rad = radians(angleDeg);
  float vx = v0 * cos(rad);
  float vy = v0 * sin(rad);
  
  float prevX = originX;
  float prevY = originY;

  int simT = 1;
  while (simT < 25) {
    float st = simT * 0.25f;
    float sx = originX + (vx * st * scale);
    float sy = originY - (((vy * st) - (0.5f * g * (st * st))) * scale);
    
    if (sy > originY) {
      break;
    }
    if (simT % 2 == 0) {
      line(prevX, prevY, sx, sy);
    }
    prevX = sx;
    prevY = sy;
    simT += 1;
  }
}

void drawUI() {
  fill(255, 255, 255, 220);
  stroke(200);
  strokeWeight(1);
  rect(15, 12, 770, 65, 12);
  
  fill(40);
  textSize(14);
  text("ANGLE: " + (int)angleDeg + " deg", 35, 42);
  text("SPEED: " + (int)v0 + " m/s", 235, 42);
  
  fill(230, 240, 250);
  stroke(150);
  rect(145, 25, 28, 25, 5);
  rect(178, 25, 28, 25, 5);
  
  rect(345, 25, 28, 25, 5);
  rect(378, 25, 28, 25, 5);
  
  fill(0);
  textSize(16);
  text("-", 155, 42);
  text("+", 187, 42);
  text("-", 355, 42);
  text("+", 387, 42);
  
  if (isFiring) {
    fill(235, 87, 87);
  } else {
    fill(46, 204, 113);
  }
  noStroke();
  rect(435, 20, 110, 36, 8);
  
  fill(52, 152, 219);
  rect(560, 20, 140, 36, 8);
  
  fill(255);
  textSize(15);
  if (isFiring) {
    text("RESET", 465, 43);
  } else {
    text("FIRE !", 468, 43);
  }
  text("NEW TARGET", 580, 43);
}

void draw() {
  drawBackground();
  drawTarget();
  
  if (!isFiring) {
    drawDottedPreview();
  }
    
  drawCannon();
  drawUI();
  
  noFill();
  stroke(231, 76, 60);
  strokeWeight(3);
  beginShape();
  for (int i = 0; i < pathX.size(); i++) {
    vertex(pathX.get(i), pathY.get(i));
  }
  endShape();

  if (isFiring) {
    float rad = radians(angleDeg);
    float vx = v0 * cos(rad);
    float vy = v0 * sin(rad);
    float xM = vx * t;
    float yM = (vy * t) - (0.5f * g * (t * t));
    
    float screenX = originX + (xM * scale);
    float screenY = originY - (yM * scale);

    pathX.add(screenX);
    pathY.add(screenY);

    fill(40);
    stroke(255, 200, 0);
    strokeWeight(1.5f);
    ellipse(screenX, screenY, 14, 14);

    if (screenX >= targetX && screenX <= (targetX + targetW) && screenY >= (originY - 15)) {
      hitTarget = true;
    }

    t = t + 0.15f;

    if (screenY >= originY && t > 0.5f) {
      isFiring = false;
    }
  }
}

void mousePressed() {
  if (mouseX >= 145 && mouseX <= 173 && mouseY >= 25 && mouseY <= 50) {
    if (angleDeg > 10 && !isFiring) {
      angleDeg -= 5;
    }
  } else if (mouseX >= 178 && mouseX <= 206 && mouseY >= 25 && mouseY <= 50) {
    if (angleDeg < 85 && !isFiring) {
      angleDeg += 5;
    }
  } else if (mouseX >= 345 && mouseX <= 373 && mouseY >= 25 && mouseY <= 50) {
    if (v0 > 10 && !isFiring) {
      v0 -= 5;
    }
  } else if (mouseX >= 378 && mouseX <= 406 && mouseY >= 25 && mouseY <= 50) {
    if (v0 < 100 && !isFiring) {
      v0 += 5;
    }
  } else if (mouseX >= 435 && mouseX <= 545 && mouseY >= 20 && mouseY <= 56) {
    if (!isFiring) {
      t = 0.0f;
      pathX.clear();
      pathY.clear();
      isFiring = true;
      hitTarget = false;
      fireEffect = 3;
    } else {
      t = 0.0f;
      pathX.clear();
      pathY.clear();
      isFiring = false;
      hitTarget = false;
    }
  } else if (mouseX >= 560 && mouseX <= 700 && mouseY >= 20 && mouseY <= 56) {
    targetX = random(300, 700);
    hitTarget = false;
  }
}
