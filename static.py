t = 0


def setup():
    size(200, 200)
    
def draw():
    global t
    loadPixels()
    for x in range(width):
        for y in range(height):
            index = x + y*width
            r = noise(t)
            r = map(r, 0, 1, 0, 256)
            pixels[index] = color(r, r, r)
            t += .1
    updatePixels()        
    print(frameRate)       
    
    
