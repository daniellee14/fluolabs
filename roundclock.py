import fluomaze as fluo 

def setup():
    size(400, 400)

    
def draw():
    background(0)
    stroke(255)
    textSize(32)
    
    h = hour()
    m = minute()
    s = second()
    
    text(str(h) + ":" + str(m) + ":" + str(s), 0, 32)
    
    translate(200, 200)
    rotate(radians(-90))
    
    # Seconds arc
    strokeWeight(4)
    noFill()
    stroke(255, 100, 150)
    sAngle = map(s, 0, 60, 0, 360)
    arc(0, 0, 300, 300, 0, radians(sAngle))
    
    pushMatrix()
    rotate(radians(sAngle))
    line(0, 0, 100, 0)
    popMatrix()
    
    # Minutes arc
    stroke(150, 100, 255)
    mAngle = map(m, 0, 60, 0, 360)
    arc(0, 0, 280, 280, 0, radians(mAngle))
    
    pushMatrix()
    rotate(radians(mAngle))
    line(0, 0, 80, 0)
    popMatrix()
   
     # hour arc
    stroke(150, 255, 100)
    hAngle = map(h % 12, 0, 12, 0, 360)
    arc(0, 0, 260, 260, 0, radians(hAngle))
    
    pushMatrix()
    rotate(radians(hAngle))
    line(0, 0, 60, 0)
    popMatrix()
