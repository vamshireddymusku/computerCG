x = 400
y = 0
z = 360
s = 1
speed = 1

def setup():
    size(800,700,P3D)
    background(255)

def draw():
    pushMatrix()
    background(255)
    move()
    display()
    popMatrix()
    
def move():
    global y
    y = y+speed
    if(y>height):
        y = 0
def rotclk():
    global z
    z = z - 0.05
    if(z==0):
        z = 360
    rotate(z)
def rotaclk():
    global s
    s = s+0.05
    if(s==360):
        s = 0
    rotate(s)
def display():
    fill(250,0,250)
    rect(x,y,20,40)
    pushMatrix()
    translate(200,300)
    rotclk()
    fill(250,0,250)
    sphere(100)
    popMatrix()
    pushMatrix()
    translate(600,300)
    rotaclk()
    sphere(100)
    popMatrix()
