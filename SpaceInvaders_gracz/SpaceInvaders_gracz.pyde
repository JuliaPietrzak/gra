global pos1
pos1=500
global pos2
pos2=250
def setup():
    rectMode(CENTER)
    size(1000,1000)
    global pos1
    pos1=500
    global pos2
    pos2=height/2+400
    noStroke()

def draw():
    background(0)
    fill(255) 
    global pos1
    global pos2
    rect(pos1,pos2,50,50)
    if keyPressed:
        if key =='D' or key =='d':
            pos1+=1
    if keyPressed:
        if key =='A' or key =='a':
            pos1-=1
    if (pos2 > height): 
        noLoop()
