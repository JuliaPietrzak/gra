class gracz():
    def __init__(self):
        self.x=500
        self.y=900
        self.lewo=0
        self.prawo=0
    def show(self):
        rect(self.x,self.y,50,50)
    def move(self):
        self.x=self.x+(self.prawo - self.lewo)
        if (self.x>975):
            self.x=975
        if (self.x<25):
            self.x=25
        global posgracza
        posgracza=self.x
        
class pocisk():
    def __init__(self):
        self.x=200
        self.y=890
        self.gora=0
    def show(self):
        ellipse(self.x,self.y,10,10)
    def move(self):
        if (self.y>=890):
            self.x=posgracza
        self.y=self.y+self.gora
        if (self.y<0):
            self.y=890
            self.gora=0
        global pociskX
        global pociskY
        pociskX=self.x
        pociskY=self.y
class przeciwnik():
    def __init__(self,x):
        self.x=200+x
        self.y=200
    def show(self):
        rect(self.x,self.y,30,30)
    def move(self):
        self.x=self.x+2
        if (self.x>950):
            self.x=50
            self.y=self.y+100



def setup():
    rectMode(CENTER)
    size(1000,1000)
    noStroke()
    global g
    global p1
    global p2
    global b
    g=gracz()
    p1=przeciwnik(100)
    p2=przeciwnik(200)
    b=pocisk()
def draw():
    background(0)
    fill(255)
    g.show()
    g.move()
    fill(255,0,0)
    p1.show()
    p1.move()
    p2.show()
    p2.move()
    b.show()
    b.move()
    if keyPressed:
        if key =='D' or key =='d':
            g.prawo=10
    if keyPressed:
        if key =='A' or key =='a':
            g.lewo=10
    if keyPressed:
        if key =='W' or key =='w':
            b.gora=-20
def keyReleased():
    if key =='D' or key =='d':
        g.prawo=0
    if key =='A' or key =='a':
        g.lewo=0
