from graph import *

import math
z=2
windowSize(1200/2, 1000/2)
canvasSize(1200/2, 1000/2)
brushColor("grey")
rectangle(0, 0, 1200/2, 1000/2)
def bs(x, y):
    brushColor("black")
    rectangle(x, y, x+5, y+5)
x=0
for i in range(120):
    y=0
    if x%2==0:
        for j in range(50):
            bs(x, y)
            y+=10
    else:
        y=5
        for k in range(49):
            bs(x, y)
            y+=10
    x+=5
brushColor(233, 198, 175)
polygon([(425/2, 1000/2),(92/2,0), (17/2, 0), (350/2, 1000/2), (425/2, 1000/2)])

polygon([(775/2, 1000/2), (1108/2,0), (1183/2,0), (850/2, 1000/2), (775/2, 1000/2)])
brushColor("orange")
circle(600/2, 1000/2, 300/2)
polygon([(310/2, 930/2), (420/2, 810/2), (345/2, 770/2), (270/2, 800/2), (250/2, 850/2), (310/2,930/2)])
polygon([(890/2, 930/2), (780/2, 810/2), (855/2, 770/2), (930/2, 800/2), (950/2, 850/2), (890/2,930/2)])
brushColor(233, 198, 175)
circle(600/2, 500/2, 250/2)
brushColor("brown")
polygon([(600/2, 500/2+15), ((600/2)+13, 500/2 + 8), ((600/2) - 13, 500/2 + 8), (600/2, 500/2+15)])
brushColor("red")
polygon([(600/2, 500/2+ 75), (600/2+ 75,500/2+30), (600/2-75, 500/2+30), (600/2, 500/2+75)])
brushColor("blue")
circle(525/2, 430/2, 60/2)
circle(675/2, 430/2, 60/2)
brushColor("black")
circle(525/2, 430/2, 20/2)
circle(675/2, 430/2, 20/2) 
def tr(x, y):
    brushColor(212, 42, 255)
    polygon([(x,y), (x+60/2*1/2, y- 60/2*(3**0.5)/2), (x-60/2*1/2,y-60/2*(3**0.5)/2)])
y=(500-110)/2
x=(600-219)/2
sidelenght=85/2
for i in range(5):
    a=math.cos(math.pi*(1/3-i/12))
    b=math.sin(math.pi*(1/3-i/12))
    c=math.cos(math.pi*(1/3+i/12))
    d=math.sin(math.pi*(1/3+i/12))
    brushColor(212, 42, 255)
    polygon([(x,y), (x+sidelenght*a, y- sidelenght*b), (x-sidelenght*c,y-sidelenght*d)])
    if i==3:
        y-=10/2
    else:
        y-=37/2
    
    x+=35/2
    
x=600/2
y=250/2
for i in range(5):
    a=math.cos(math.pi*(1/3-5/12-i/12))
    b=math.sin(math.pi*(1/3-5/12-i/12))
    c=math.cos(math.pi*(1/3+5/12+i/12))
    d=math.sin(math.pi*(1/3+5/12+i/12))
    brushColor(212, 42, 255)
    polygon([(x,y), (x+sidelenght*a, y- sidelenght*b), (x-sidelenght*c,y-sidelenght*d)])
    
    if i==3:
        x+=40/2
    elif i==0:
        x+=80/2
    else:
        x+=50/2
    y+=35/2
#brushColor(233, 198, 175)
#circle(123/2 , 150/2, 90/2)
#circle(1077/2, 150/2, 90/2)
a=70/2
b=(110/2)
x=123/2
y=60/2
s=[(x, y)]
y=150/2-b

for i in range(2*int(b)):
    x=(123/2-a*((1-((y-150/2)**2)/(b**2))**2)**0.25)
    
    coord=(x, y)
    s.append(coord)
    y+=1
for i in range(2*int(b)):
    x=(123/2+a*((1-((y-150/2)**2)/(b**2))**2)**0.25)
    
    coord=(x, y)
    s.append(coord)
    y-=1

brushColor(233, 198, 175)
polygon(s)


x=1077/2
y=60/2
s=[(x, y)]
y=150/2-b

for i in range(2*int(b)):
    x=(1077/2-a*((1-((y-150/2)**2)/(b**2))**2)**0.25)
    
    coord=(x, y)
    s.append(coord)
    y+=1
for i in range(2*int(b)):
    x=(1077/2+a*((1-((y-150/2)**2)/(b**2))**2)**0.25)
    
    coord=(x, y)
    s.append(coord)
    y-=1

brushColor(233, 198, 175)
polygon(s)

brushColor("green")
rectangle(0, 0, 1200/2, 160/2)
penSize(5)
penColor(0, 0, 0)
#py
line(10/z, 130/z, 10/z, 30/z)
line(10/z, 30/z, 50/z, 30/z)
line(50/z, 30/z, 50/z, 80/z)
line(50/z, 80/z, 10/z, 80/z)
line(105/z, 105/z, 75/z, 30/z)
line(105/z, 105/z, 135/z, 30/z)
line(105/z, 105/z, 105/z, 145/z)
#th
line(145/z, 30/z, 200/z, 30/z)
line(175/z, 30/z, 175/z, 130/z)
line(220/z, 30/z, 220/z, 130/z)
line(220/z, 80/z, 270/z, 80/z)
line(270/z, 30/z, 270/z, 130/z)
#on
line(295/z, 30/z, 295/z, 130/z)
line(295/z, 130/z, 340/z, 130/z)
line(340/z, 130/z, 340/z, 30/z)
line(340/z, 30/z, 295/z, 30/z)
line(360/z, 130/z, 360/z, 30/z)
line(360/z, 30/z, 410/z, 130/z)
line(410/z, 130/z, 410/z, 30/z)
# is 
line(525/z, 20/z, 525/z, 25/z)
line(525/z, 30/z, 525/z, 130/z)
line(620/z, 30/z, 570/z, 30/z)
line(570/z, 30/z, 570/z, 80/z)
line(570/z, 80/z, 620/z, 80/z)
line(620/z, 80/z, 620/z, 130/z)
line(620/z, 130/z, 570/z, 130/z)
#am
line(710/z, 130/z, 735/z, 30/z)
line(735/z, 30/z, 760/z, 130/z)
line(722.5/z, 80/z, 757.5/z, 80/z)
line(780/z, 130/z, 780/z, 30/z)
line(780/z, 30/z, 805/z, 80/z)
line(805/z, 80/z, 830/z, 30/z)
line(830/z, 30/z, 830/z, 130/z)
#az
line(850/z, 130/z, 875/z, 30/z)
line(875/z, 30/z, 900/z, 130/z)
line(862.5/z, 80/z, 887.5/z, 80/z)
line(920/z, 30/z, 970/z, 30/z)
line(970/z, 30/z, 920/z, 130/z)
line(920/z, 130/z, 970/z, 130/z)
#ing
line(1015/z, 20/z, 1015/z, 25/z)
line(1015/z, 30/z, 1015/z, 130/z)
line(1060/z, 130/z, 1060/z, 30/z)
line(1060/z, 30/z, 1110/z, 130/z)
line(1110/z, 130/z, 1110/z, 30/z)
line(1180/z, 30/z, 1130/z, 30/z)
line(1130/z, 30/z, 1130/z, 130/z)
line(1130/z, 130/z, 1180/z, 130/z)
line(1180/z, 130/z, 1180/z, 80/z)
line(1180/z, 80/z, 1153/z, 80/z)

run()
