star_x = []
star_y = []
speed = []
dias = []


def setup():
    #size(800, 800)
    fullScreen()
    background(0)
    for i in range(400):
        star_x.append(random(width))
        star_y.append(random(height))
        speed.append(random(0.1, 1))
        dias.append(random(4, 8))
    
def draw():

    fill(map(mouseX, 0, width, 0, 256), 0, 0)
    
    for i in range(len(star_x)):
        # show star
        ellipse(star_x[i], star_y[i], dias[i], dias[i])
        
        # update
        star_x[i] += speed[i]
        star_y[i] += speed[i]
        
        # check
        if (star_x[i] - dias[i]/2 > width):
            star_x[i] = random(width)
        if (star_y[i] - dias[i]/2 > height):
            star_y[i] = random(height)
        
    
def mouseClicked():
    star_x.append(mouseX)
    star_y.append(mouseY)
    speed.append(random(0.1, 1))
    
def keyPressed():
    if (key == ' '):
        background(0)
        del star_x[:]
        del star_y[:]
        del speed[:]
        del dias[:]
    
