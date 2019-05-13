global poz1
poz1=0
global poz2
poz2=0
def setup():
    size(1000,1000)
    rectMode(CENTER)
    global poz1
    poz1=height/2
    global poz2
    poz2=width/4
def draw():
    background(0)
    fill(255,0,0)
    global poz1
    global poz2
    rect(poz1, poz2, 40, 40)
    poz1+=1
    if (poz1 > width):
        poz1-=1000
    if (poz1 < 0):
        poz1+=1
