word = "PROGRAMMING"

def setup():
    size(600, 300)
    textSize(40)

def draw():
    background(255)
    i = 0
    while i < len(word):
        c = word[i]
        code = ord(c)
        fill(code * 2, 100, 200)
        text(c, mouseX + i * 35, mouseY)
        textSize(12)
        text(str(code), mouseX + i * 35, mouseY + 20)
        textSize(40)
        i = i + 1
