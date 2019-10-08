#!/usr/bin/python
# -*- coding: utf-8 -*-
import graph as g

import math

# z is size

z = 2
g.windowSize(1200 / z, 1000 / z)
g.canvasSize(1200 / z, 1000 / z)
g.brushColor('grey')

# background

g.rectangle(0, 0, 1200 / z, 1000 / z)


def bs(x, y):
    g.brushColor('black')
    g.rectangle(x, y, x + 10 / z, y + 10 / z)


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

g.brushColor(233, 198, 175)
g.polygon([(425 / z, 1000 / z), (92 / z, 0), (17 / z, 0),
           (350 / z, 1000 / z), (425 / z, 1000 / z)])

g.polygon([(775 / z, 1000 / z), (1108 / z, 0), (1183 / z, 0),
           (850 / z, 1000 / z), (775 / z, 1000 / z)])

# body

g.brushColor('orange')
g.circle(600 / z, 1000 / z, 300 / z)
g.polygon([
    (310 / z, 930 / z),
    (420 / z, 810 / z),
    (345 / z, 770 / z),
    (270 / z, 800 / z),
    (250 / z, 850 / z),
    (310 / z, 930 / z),
])
g.polygon([
    (890 / z, 930 / z),
    (780 / z, 810 / z),
    (855 / z, 770 / z),
    (930 / z, 800 / z),
    (950 / z, 850 / z),
    (890 / z, 930 / z),
])

# face

g.brushColor(233, 198, 175)
g.circle(600 / z, 500 / z, 250 / z)

# nose

g.brushColor('brown')
g.polygon([(600 / z, 500 / z + 30 / z), (600 / z + 26 / z, 500 / z + 16 / z), 
           (600 / z - 26 / z, 500 / z + 16 / z),
           (600 / z, 500 / z + 30 / z)])

# mouth

g.brushColor('red')
m = 1
mouth_help = g.rectangle(0, 0, 1, 1)
step = 0


def update_mouth():
    step = g.xCoord(mouth_help)
    global m
    m = 1 / (step + 2)
    g.brushColor('red')
    mouth = g.polygon([(600 / z, 500 / z + 150 / z), 
                       (600 / z + 150 * m / z, 500 / z + 60 / z),
                       (600 / z - 150 * m / z, 500 / z + 60 / z),
                       (600 / z, 500 / z + 150 / z)])
    step += 1
    if step >= 7:
        g.moveObjectBy(mouth_help, -7, 0)


g.onTimer(update_mouth)

# eyes
colors = ('green', 'blue', 'red', 'yellow',
          'black', 'white', 'orange', 'magenta')

g.brushColor('blue')
eye_1 = g.circle(525 / z, 430 / z, 60 / z)
eye_2 = g.circle(675 / z, 430 / z, 60 / z)
help_obj_eye_1 = g.rectangle(0, 0, 1, 1)
g.changeFillColor(help_obj_eye_1, 'green')


def update_eye_1():
    g.moveObjectBy(help_obj_eye_1, 1, 0)
    g.changeFillColor(eye_1, colors[g.xCoord(help_obj_eye_1)])
    if g.xCoord(help_obj_eye_1) >= 6:
        g.moveObjectBy(help_obj_eye_1, - 6, 0)


g.onTimer(update_eye_1)
help_obj_eye_2 = g.rectangle(0, 0, 1, 1)
g.changeFillColor(help_obj_eye_2, 'green')


def update_eye_2():
    g.moveObjectBy(help_obj_eye_2, 1, 0)
    g.moveObjectBy(eye_2, 5 / z, 5 / z)
    if g.xCoord(eye_2) >= 625 / z:
        g.moveObjectBy(eye_2, - 20 / z, -20 / z)
    g.changeFillColor(eye_2, colors[g.xCoord(help_obj_eye_2)])
    if g.xCoord(help_obj_eye_2) >= 6:
        g.moveObjectBy(help_obj_eye_2, - 6, 0)


g.onTimer(update_eye_2)

g.brushColor('black')
inner_eye_1 = g.circle(525 / z, 430 / z, 20 / z)
g.circle(675 / z, 430 / z, 20 / z)
r = 40 / z
x = 0
y = 370 / z
s_circle = []
for i in range(2 * int(r)):
    x = 515 / z - ((r ** 2 - (y - 410 / z) ** 2) ** 2) ** 0.25

    coord_1 = x
    coord_2 = y
    s_circle.append(coord_1)
    s_circle.append(coord_2)
    y += 1
for i in range(2 * int(r)):
    x = 515 / z + ((r ** 2 - (y - 410 / z) ** 2) ** 2) ** 0.25

    coord_1 = x
    coord_2 = y
    s_circle.append(coord_1)
    s_circle.append(coord_2)
    y -= 1
circle_help_object = g.rectangle(0, 0, 1, 1)


def update_inner_eye():
    g.moveObjectBy(circle_help_object, 1, 0)
    g.moveObjectTo(inner_eye_1, s_circle[2 * int(g.xCoord(circle_help_object))],
                   s_circle[2 * int(g.xCoord(circle_help_object)) - 1])
    if g.xCoord(circle_help_object) >= 79:
        g.moveObjectBy(circle_help_object, - 79, 0)


g.onTimer(update_inner_eye)


# haircut

def tr(x, y):
    g.brushColor(212, 42, 255)
    g.polygon([(x, y), (x + 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2),
               (x - 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2)])


y = (500 - 110) / z
x = (600 - 219) / z
sidelenght = 85 / z
for i in range(5):
    a = math.cos(math.pi * (1 / 3 - i / 12))
    b = math.sin(math.pi * (1 / 3 - i / 12))
    c = math.cos(math.pi * (1 / 3 + i / 12))
    d = math.sin(math.pi * (1 / 3 + i / 12))
    g.brushColor(212, 42, 255)
    g.polygon([(x, y), (x + sidelenght * a, y - sidelenght * b),
               (x - sidelenght * c, y - sidelenght * d)])
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
    g.brushColor(212, 42, 255)
    g.polygon([(x, y), (x + sidelenght * a, y - sidelenght * b),
               (x - sidelenght * c, y - sidelenght * d)])

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

g.brushColor(233, 198, 175)
g.polygon(s)

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

g.brushColor(233, 198, 175)
g.polygon(s)

"""
def draw_human(xc):

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
        x+=10/z

    # grid
    # arms

    brushColor(233, 198, 175)
    polygon([(425 / z + xc / z, 1000 / z), (92 / z + xc / z, 0),
    (17 / z + xc / z, 0), (350 / z + xc / z, 1000 / z),
             (425 / z + xc / z, 1000 / z)])

    polygon([(775 / z + xc / z, 1000 / z), (1108 / z + xc / z, 0), 
    (1183 / z + xc / z, 0), (850 / z + xc / z, 1000 / z),
             (775 / z + xc / z, 1000 / z)])

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
    polygon([(600 / z + xc / z, 500 / z + 30 / z), 
    (600 / z + xc / z + 26 / z, 500 / z + 16 / z),
             (600 / z + xc / z - 26 / z, 500 / z + 16 / z), 
             (600 / z + xc / z, 500 / z + 30 / z)])

    # mouth

    brushColor('red')
    polygon([(600 / z + xc / z, 500 / z + 150 / z), 
    (600 / z + xc / z + 150 / z, 500 / z + 60 / z),
             (600 / z - 150 / z + xc / z, 500 / z + 60 / z),
             (600 / z + xc / z, 500 / z + 150 / z)])

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
        polygon([(x + xc / z, y), 
        (x + xc / z + 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2),
                 (x + xc / z - 60 / z * 1 / 2, y - 60 / z * 3 ** 0.5 / 2)])

    y = (500 - 110) / z
    x = (600 - 219) / z
    sidelength = 85 / z
    for i in range(5):
        a = math.cos(math.pi * (1 / 3 - i / 12))
        b = math.sin(math.pi * (1 / 3 - i / 12))
        c = math.cos(math.pi * (1 / 3 + i / 12))
        d = math.sin(math.pi * (1 / 3 + i / 12))
        brushColor(212, 42, 255)
        polygon([(x + xc / z, y),
        (x + xc / z + sidelength * a, y - sidelength * b),
                 (x + xc / z - sidelength * c, y - sidelength * d)])
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
        (x + xc / z + sidelength * a, y - sidelength * b),
                 (x + xc / z - sidelength * c, y - sidelength * d)])

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
"""
# banner: python is amazing

g.brushColor('green')
g.rectangle(0, 0, 1200 / z, 160 / z)
help_obj = g.rectangle(0, 0, 1, 1)
g.penSize(5)


def letters(f: object, s: object, t: object) -> object:
    g.penColor(f, s, t)

    # py

    g.line(10 / z, 130 / z, 10 / z, 30 / z)
    g.line(10 / z, 30 / z, 50 / z, 30 / z)
    g.line(50 / z, 30 / z, 50 / z, 80 / z)
    g.line(50 / z, 80 / z, 10 / z, 80 / z)
    g.line(105 / z, 105 / z, 75 / z, 30 / z)
    g.line(105 / z, 105 / z, 135 / z, 30 / z)
    g.line(105 / z, 105 / z, 105 / z, 145 / z)

    # th

    g.line(145 / z, 30 / z, 200 / z, 30 / z)
    g.line(175 / z, 30 / z, 175 / z, 130 / z)
    g.line(220 / z, 30 / z, 220 / z, 130 / z)
    g.line(220 / z, 80 / z, 270 / z, 80 / z)
    g.line(270 / z, 30 / z, 270 / z, 130 / z)

    # on

    g.line(295 / z, 30 / z, 295 / z, 130 / z)
    g.line(295 / z, 130 / z, 340 / z, 130 / z)
    g.line(340 / z, 130 / z, 340 / z, 30 / z)
    g.line(340 / z, 30 / z, 295 / z, 30 / z)
    g.line(360 / z, 130 / z, 360 / z, 30 / z)
    g.line(360 / z, 30 / z, 410 / z, 130 / z)
    g.line(410 / z, 130 / z, 410 / z, 30 / z)

    # is

    g.line(525 / z, 20 / z, 525 / z, 25 / z)
    g.line(525 / z, 30 / z, 525 / z, 130 / z)
    g.line(620 / z, 30 / z, 570 / z, 30 / z)
    g.line(570 / z, 30 / z, 570 / z, 80 / z)
    g.line(570 / z, 80 / z, 620 / z, 80 / z)
    g.line(620 / z, 80 / z, 620 / z, 130 / z)
    g.line(620 / z, 130 / z, 570 / z, 130 / z)

    # am

    g.line(710 / z, 130 / z, 735 / z, 30 / z)
    g.line(735 / z, 30 / z, 760 / z, 130 / z)
    g.line(722.5 / z, 80 / z, 757.5 / z, 80 / z)
    g.line(780 / z, 130 / z, 780 / z, 30 / z)
    g.line(780 / z, 30 / z, 805 / z, 80 / z)
    g.line(805 / z, 80 / z, 830 / z, 30 / z)
    g.line(830 / z, 30 / z, 830 / z, 130 / z)

    # az

    g.line(850 / z, 130 / z, 875 / z, 30 / z)
    g.line(875 / z, 30 / z, 900 / z, 130 / z)
    g.line(862.5 / z, 80 / z, 887.5 / z, 80 / z)
    g.line(920 / z, 30 / z, 970 / z, 30 / z)
    g.line(970 / z, 30 / z, 920 / z, 130 / z)
    g.line(920 / z, 130 / z, 970 / z, 130 / z)

    # ing

    g.line(1015 / z, 20 / z, 1015 / z, 25 / z)
    g.line(1015 / z, 30 / z, 1015 / z, 130 / z)
    g.line(1060 / z, 130 / z, 1060 / z, 30 / z)
    g.line(1060 / z, 30 / z, 1110 / z, 130 / z)
    g.line(1110 / z, 130 / z, 1110 / z, 30 / z)
    g.line(1180 / z, 30 / z, 1130 / z, 30 / z)
    g.line(1130 / z, 30 / z, 1130 / z, 130 / z)
    g.line(1130 / z, 130 / z, 1180 / z, 130 / z)
    g.line(1180 / z, 130 / z, 1180 / z, 80 / z)
    g.line(1180 / z, 80 / z, 1153 / z, 80 / z)


def change_color():
    g.moveObjectBy(help_obj, 10, 0)
    letters(g.xCoord(help_obj), g.xCoord(help_obj), g.xCoord(help_obj))
    if g.xCoord(help_obj) >= 200:
        g.moveObjectBy(help_obj, -200, 0)


g.onTimer(change_color)

# bow-tie

side = 60
bow_help = g.rectangle(0, 0, 1, 1)


def update_bow_tie():
    global side
    angle = g.xCoord(bow_help)
    a_mult = math.cos(math.pi * (1 / 3 - angle / 36))
    b_mult = math.sin(math.pi * (1 / 3 - angle / 36))
    c_mult = math.cos(math.pi * (1 / 3 + angle / 36))
    d_mult = math.sin(math.pi * (1 / 3 + angle / 36))
    g.brushColor('black')
    bow_tie = g.polygon([(600 / z, 850 / z),
                         (600 / z + side * a_mult / z,
                          850 / z - side * b_mult / z),
                         (600 / z + side * c_mult / z,
                          850 / z + side * d_mult / z),
                         (600 / z, 850 / z),
                         (600 / z - side * c_mult / z,
                          850 / z - side * d_mult / z),
                         (600 / z - side * a_mult / z,
                          850 / z + side * b_mult / z),
                         (600 / z, 850 / z)])
    g.moveObjectBy(bow_help, 1, 0)
    if g.xCoord(bow_help) >= 72:
        g.moveObjectBy(bow_help, -72, 0)


g.onTimer(update_bow_tie)


g.run()
