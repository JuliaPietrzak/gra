class Przeciwnik:
    def __init__(self, x, y, w, h, c):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c=c
    def move(self):
        x+=1
        if (x > width):
            x-=1000
        if (x < 0):
            x+=1
    #def life(self):
        #jeżeli kolor czerwony dotknie koloru żółty(pocisk) to znika
            
x=height/2
y=width/4
w=30
h=30
c=fill(255,0,0)
