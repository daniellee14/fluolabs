x = 50
xSpeed = 1
col = 255
recWidth = 500
strike = 0

def setup():
    size(800, 800)
    fullScreen()
    
def draw():
    global x, strike
    background(0)
    fill(col, 0, 0)
    rect(x, height/2, recWidth, 75)
    
    x = x + xSpeed
    fill(255)
    text("xSpeed: " + str(xSpeed) + " strike:" + str(strike), width/2, 32)
    if (strike == 3):
        textSize(60)
        text("Game over, man!", width/2 - 150, height/2)
        noLoop()
        
    # check right boundary
    if (x > width):
        x = -1 * recWidth
        strike += 1
        
    # check left boundary
    if (x < -1 * recWidth):
        x = width
        strike += 1
        
        
    
def mouseClicked():
    global xSpeed, col, recWidth
    
    if ((mouseX > x) and (mouseX < x + recWidth)):
        if ((mouseY > height/2) and (mouseY < height/2 + 75)):
            xSpeed = xSpeed * -1
            
            if (recWidth > 100):
                recWidth = recWidth - 10
                    
            
            col = random(100, 255)
            if (xSpeed > 0):
                xSpeed = xSpeed + 1
            elif (xSpeed < 0):
                xSpeed = xSpeed - 1
        
