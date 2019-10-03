#!/usr/bin/python
# -*- coding: utf-8 -*-
from graph import *

import math

# z is size

z = 2
windowSize(1200 / z + 1200 / z, 1000 / z)
canvasSize(1200 / z + 1200 / z, 1000 / z)
brushColor('grey')

# background

rectangle(0, 0, 1200 / z, 1000 / z)


def bs(x, y):
    brushColor('black')
    rectangle(x, y, x + 10 / z, y + 10 / z)


x = 0
for i in range(120):
    y = 0
    if x % (4 / z) == 0:
        for j in range(50):
            bs(x, y)
            y += 20 / z
    else:
        y = 10 / z
        for k in range(49):
            bs(x, y)
            y += 20 / z
    x += 10 / z

# arms

brushColor(233, 198, 175)
polygon([(425 / z, 1000 / z), (92 / z, 0), (17 / z, 0), (350 / z, 1000 / z), (425 / z, 1000 / z)])

polygon([(775 / z, 1000 / z), (1108 / z, 0), (1183 / z, 0), (850 / z, 1000 / z), (775 / z, 1000 / z)])

# body

brushColor('orange')
circle(600 / z, 1000 / z, 300 / z)
polygon([
    (310 / z, 930 / z),
    (420 / z, 810 / z),
    (345 / z, 770 / z),
    (270 / z, 800 / z),
    (250 / z, 850 / z),
    (310 / z, 930 / z),
    ])
polygon([
    (890 / z, 930 / z),
    (780 / z, 810 / z),
    (855 / z, 770 / z),
    (930 / z, 800 / z),
    (950 / z, 850 / z),
    (890 / z, 930 / z),
    ])

# face

brushColor(233, 198, 175)
circle(600 / z, 500 / z, 250 / z)

# nose

brushColor('brown')
polygon([(600 / z, 500 / z + 30 / z), (600 / z + 26 / z, 500 / z + 16 / z), (600 / z - 26 / z, 500 / z + 16 / z), (600 / z, 500 / z + 30 / z)])

# mouth

brushColor('red')
polygon([(600 / z, 500 / z + 150 / z), (600 / z + 150 / z, 500 / z + 60 / z), (600 / z - 150 / z, 500 / z + 60 / z), (600 / z, 500 / z + 150 / z)])

# eyes

brushColor('blue')
circle(525 / z, 430 / z, 60 / z)
circle(675 / z, 430 / z, 60 / z)
brushColor('black')
circle(525 / z, 430 / z, 20 / z)
circle(675 / z, 430 / z, 20 / z)


# haircut

def tr(x, y):
    brushColor(212, 42, 255)
    polygon([(x, y), (x + 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2), (x - 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2)])


y = (500 - 110) / z
x = (600 - 219) / z
sidelenght = 85 / z
for i in range(5):
    a = math.cos(math.pi * (1 / 3 - i / 12))
    b = math.sin(math.pi * (1 / 3 - i / 12))
    c = math.cos(math.pi * (1 / 3 + i / 12))
    d = math.sin(math.pi * (1 / 3 + i / 12))
    brushColor(212, 42, 255)
    polygon([(x, y), (x + sidelenght * a, y - sidelenght * b), (x - sidelenght * c, y - sidelenght * d)])
    if i == 3:
        y -= 10 / z
    else:
        y -= 37 / z

    x += 35 / z

x = 600 / z
y = 250 / z
for i in range(5):
    a = math.cos(math.pi * (1 / 3 - 5 / 12 - i / 12))
    b = math.sin(math.pi * (1 / 3 - 5 / 12 - i / 12))
    c = math.cos(math.pi * (1 / 3 + 5 / 12 + i / 12))
    d = math.sin(math.pi * (1 / 3 + 5 / 12 + i / 12))
    brushColor(212, 42, 255)
    polygon([(x, y), (x + sidelenght * a, y - sidelenght * b), (x - sidelenght * c, y - sidelenght * d)])

    if i == 3:
        x += 40 / z
    elif i == 0:
        x += 80 / z
    else:
        x += 50 / z
    y += 35 / z

# brushColor(233, 198, 175)
# circle(123/2 , 150/2, 90/2)
# circle(1077/2, 150/2, 90/2)
# hands

a = 70 / z
b = 110 / z
x = 123 / z
y = 60 / z
s = [(x, y)]
y = 150 / z - b

for i in range(2 * int(b)):
    x = 123 / z - a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

    coord = (x, y)
    s.append(coord)
    y += 1
for i in range(2 * int(b)):
    x = 123 / z + a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

    coord = (x, y)
    s.append(coord)
    y -= 1

brushColor(233, 198, 175)
polygon(s)

x = 1077 / z
y = 60 / z
s = [(x, y)]
y = 150 / z - b

for i in range(2 * int(b)):
    x = 1077 / z - a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

    coord = (x, y)
    s.append(coord)
    y += 1
for i in range(2 * int(b)):
    x = 1077 / z + a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

    coord = (x, y)
    s.append(coord)
    y -= 1

brushColor(233, 198, 175)
polygon(s)


def draw_human(xc):
    """
    x=xc
    for i in range(120):
        y=0
        if x%(4/z)==0:
            for j in range(50):
                bs(x, y)
                y+=20/z
        else:
            y=10/z
            for k in range(49):
                bs(x, y)
                y+=20/z
        x+=10/z"""

    # grid
    # arms

    brushColor(233, 198, 175)
    polygon([(425 / z + xc / z, 1000 / z), (92 / z + xc / z, 0), (17 / z + xc / z, 0), (350 / z + xc / z, 1000 / z), (425 / z + xc / z, 1000 / z)])

    polygon([(775 / z + xc / z, 1000 / z), (1108 / z + xc / z, 0), (1183 / z + xc / z, 0), (850 / z + xc / z, 1000 / z), (775 / z + xc / z, 1000 / z)])

    # body

    brushColor('orange')
    circle(600 / z + xc / z, 1000 / z, 300 / z)
    polygon([
        (310 / z + xc / z, 930 / z),
        (420 / z + xc / z, 810 / z),
        (345 / z + xc / z, 770 / z),
        (270 / z + xc / z, 800 / z),
        (250 / z + xc / z, 850 / z),
        (310 / z + xc / z, 930 / z),
        ])
    polygon([
        (890 / z + xc / z, 930 / z),
        (780 / z + xc / z, 810 / z),
        (855 / z + xc / z, 770 / z),
        (930 / z + xc / z, 800 / z),
        (950 / z + xc / z, 850 / z),
        (890 / z + xc / z, 930 / z),
        ])

    # face

    brushColor(233, 198, 175)
    circle(600 / z + xc / z, 500 / z, 250 / z)

    # nose

    brushColor('brown')
    polygon([(600 / z + xc / z, 500 / z + 30 / z), (600 / z + xc / z + 26 / z, 500 / z + 16 / z), (600 / z + xc / z - 26 / z, 500 / z + 16 / z), (600 / z + xc / z, 500 / z + 30 / z)])

    # mouth

    brushColor('red')
    polygon([(600 / z + xc / z, 500 / z + 150 / z), (600 / z + xc / z + 150 / z, 500 / z + 60 / z), (600 / z - 150 / z + xc / z, 500 / z + 60 / z), (600 / z + xc / z, 500 / z + 150 / z)])

    # eyes

    brushColor('blue')
    circle(525 / z + xc / z, 430 / z, 60 / z)
    circle(675 / z + xc / z, 430 / z, 60 / z)
    brushColor('black')
    circle(525 / z + xc / z, 430 / z, 20 / z)
    circle(675 / z + xc / z, 430 / z, 20 / z)

    # haircut

    def tr(x, y):
        brushColor(212, 42, 255)
        polygon([(x + xc / z, y), (x + xc / z + 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2), (x + xc / z - 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2)])

    y = (500 - 110) / z
    x = (600 - 219) / z
    sidelenght = 85 / z
    for i in range(5):
        a = math.cos(math.pi * (1 / 3 - i / 12))
        b = math.sin(math.pi * (1 / 3 - i / 12))
        c = math.cos(math.pi * (1 / 3 + i / 12))
        d = math.sin(math.pi * (1 / 3 + i / 12))
        brushColor(212, 42, 255)
        polygon([(x + xc / z, y), (x + xc / z + sidelenght * a, y - sidelenght * b), (x + xc / z - sidelenght * c, y - sidelenght * d)])
        if i == 3:
            y -= 10 / z
        else:
            y -= 37 / z

        x += 35 / z

    x = 600 / z
    y = 250 / z
    for i in range(5):
        a = math.cos(math.pi * (1 / 3 - 5 / 12 - i / 12))
        b = math.sin(math.pi * (1 / 3 - 5 / 12 - i / 12))
        c = math.cos(math.pi * (1 / 3 + 5 / 12 + i / 12))
        d = math.sin(math.pi * (1 / 3 + 5 / 12 + i / 12))
        brushColor(212, 42, 255)
        polygon([(x + xc / z, y),
            (x + xc / z + sidelenght * a, y - sidelenght * b), (x + xc / z - sidelenght * c, y - sidelenght * d)])

        if i == 3:
            x += 40 / z
        elif i == 0:
            x += 80 / z
        else:
            x += 50 / z
        y += 35 / z

    # brushColor(233, 198, 175)
    # circle(123/2 , 150/2, 90/2)
    # circle(1077/2, 150/2, 90/2)
    # hands

    a = 70 / z
    b = 110 / z
    x = 123 / z + xc / z
    y = 60 / z
    s = [(x, y)]
    y = 150 / z - b

    for i in range(2 * int(b)):
        x = 123 / z + xc / z - a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

        coord = (x, y)
        s.append(coord)
        y += 1
    for i in range(2 * int(b)):
        x = 123 / z + xc / z + a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

        coord = (x, y)
        s.append(coord)
        y -= 1

        brushColor(233, 198, 175)
        polygon(s)

    x = 1077 / z + xc / z
    y = 60 / z
    s = [(x, y)]
    y = 150 / z - b

    for i in range(2 * int(b)):
        x = 1077 / z + xc / z - a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

        coord = (x, y)
        s.append(coord)
        y += 1
    for i in range(2 * int(b)):
        x = 1077 / z + xc / z + a * ((1 - (y - 150 / z) ** 2 / b ** 2) ** 2) ** 0.25

        coord = (x, y)
        s.append(coord)
        y -= 1
    brushColor(233, 198, 175)
    polygon(s)


# end of function
# create new human

draw_human(1200)

# banner: python is amazing

brushColor('green')
rectangle(0, 0, 1200 / z, 160 / z)
penSize(5)
penColor(0, 0, 0)

# py

line(10 / z, 130 / z, 10 / z, 30 / z)
line(10 / z, 30 / z, 50 / z, 30 / z)
line(50 / z, 30 / z, 50 / z, 80 / z)
line(50 / z, 80 / z, 10 / z, 80 / z)
line(105 / z, 105 / z, 75 / z, 30 / z)
line(105 / z, 105 / z, 135 / z, 30 / z)
line(105 / z, 105 / z, 105 / z, 145 / z)

# th

line(145 / z, 30 / z, 200 / z, 30 / z)
line(175 / z, 30 / z, 175 / z, 130 / z)
line(220 / z, 30 / z, 220 / z, 130 / z)
line(220 / z, 80 / z, 270 / z, 80 / z)
line(270 / z, 30 / z, 270 / z, 130 / z)

# on

line(295 / z, 30 / z, 295 / z, 130 / z)
line(295 / z, 130 / z, 340 / z, 130 / z)
line(340 / z, 130 / z, 340 / z, 30 / z)
line(340 / z, 30 / z, 295 / z, 30 / z)
line(360 / z, 130 / z, 360 / z, 30 / z)
line(360 / z, 30 / z, 410 / z, 130 / z)
line(410 / z, 130 / z, 410 / z, 30 / z)

# is

line(525 / z, 20 / z, 525 / z, 25 / z)
line(525 / z, 30 / z, 525 / z, 130 / z)
line(620 / z, 30 / z, 570 / z, 30 / z)
line(570 / z, 30 / z, 570 / z, 80 / z)
line(570 / z, 80 / z, 620 / z, 80 / z)
line(620 / z, 80 / z, 620 / z, 130 / z)
line(620 / z, 130 / z, 570 / z, 130 / z)

# am

line(710 / z, 130 / z, 735 / z, 30 / z)
line(735 / z, 30 / z, 760 / z, 130 / z)
line(722.5 / z, 80 / z, 757.5 / z, 80 / z)
line(780 / z, 130 / z, 780 / z, 30 / z)
line(780 / z, 30 / z, 805 / z, 80 / z)
line(805 / z, 80 / z, 830 / z, 30 / z)
line(830 / z, 30 / z, 830 / z, 130 / z)

# az

line(850 / z, 130 / z, 875 / z, 30 / z)
line(875 / z, 30 / z, 900 / z, 130 / z)
line(862.5 / z, 80 / z, 887.5 / z, 80 / z)
line(920 / z, 30 / z, 970 / z, 30 / z)
line(970 / z, 30 / z, 920 / z, 130 / z)
line(920 / z, 130 / z, 970 / z, 130 / z)

# ing

line(1015 / z, 20 / z, 1015 / z, 25 / z)
line(1015 / z, 30 / z, 1015 / z, 130 / z)
line(1060 / z, 130 / z, 1060 / z, 30 / z)
line(1060 / z, 30 / z, 1110 / z, 130 / z)
line(1110 / z, 130 / z, 1110 / z, 30 / z)
line(1180 / z, 30 / z, 1130 / z, 30 / z)
line(1130 / z, 30 / z, 1130 / z, 130 / z)
line(1130 / z, 130 / z, 1180 / z, 130 / z)
line(1180 / z, 130 / z, 1180 / z, 80 / z)
line(1180 / z, 80 / z, 1153 / z, 80 / z)

run()
