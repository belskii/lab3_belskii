
from random import randrange as rnd, choice
from tkinter import mainloop, BOTH, Canvas, Frame, Tk
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class Ball:
    def __init__(self, g, x, y, r, a, type):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0  # speed
        self.vy = 0  # speed
        self.color = choice(['blue', 'green', 'red', 'brown', 'black', 'orange', 'yellow'])
        self.type = type
        if self.type == 1:
            self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                       fill=self.color)
        elif self.type == 2:
            self.id = canv.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                            fill=self.color)
        elif self.type == 3:
            ang = 72 / 180 * math.pi
            b = 2 * self.r * math.cos(54 / 180 * math.pi)  # side
            b1 = b * math.cos(ang)
            b2 = b * math.sin(ang)
            b12 = b * math.cos(ang / 2)
            b22 = b * math.sin(ang / 2)
            ang = 54 / 180 * math.pi
            x1 = b / 2
            y1 = self.r * math.sin(ang)
            points = [(self.x - x1, self.y - y1), (self.x - b1 - x1, self.y + b2 - y1),
                      (self.x + b12 - x1 - b1, self.y + b2 + b22 - y1),
                      (self.x + b + b1 - x1, self.y + b2 - y1), (self.x + b - x1, self.y - y1),
                      (self.x - x1, self.y - y1)]
            self.id = canv.create_polygon(points, fill=self.color, outline="black")
        elif self.type == 4:
            n = self.type + 2
            sid = 2 * r * math.cos((90 - 180 / n) / 180 * math.pi)
            angl = (90 - 180 / n) / 180 * math.pi
            x1 = sid / 2
            y1 = r * math.sin(angl)
            points = [(x - x1, y - y1), (x - r, y), (x - x1, y + y1),
                      (x + x1, y + y1), (x + r, y), (x + x1, y - y1),
                      (x - x1, y - y1)]
            self.id = canv.create_polygon(points, fill=self.color, outline="black")
        self.live = 100  # time of live
        self.game = g
        self.a = a  # a=0 start ball, a=1 fragment

    def move(self):
        if self.y <= 550:
            self.vy -= 0.7
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            canv.move(self.id, self.vx, -self.vy)
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 550
        if self.a == 0:
            if self.live == 60:  # if live == 60, separation happens
                self.game.balls.pop(self.game.balls.index(self))
                canv.delete(self.id)
                self.separation()
            else:
                self.live -= 1
        if self.a == 1:
            if self.live <= 0:
                self.game.balls.pop(self.game.balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 1.3
            self.x = 780

    def hittest(self, ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False

    def separation(self):
        n = rnd(3, 4)
        separetedballs = [Ball(self.game, self.x + rnd(5, 10), self.y + rnd(5, 10), 10, 1, rnd(1, 5)) for _ in range(n)]
        for i in range(n):
            separetedballs[i].vx = rnd(-10, 10)
            separetedballs[i].vy = rnd(-10, 10)
            self.game.balls += [separetedballs[i]]


class Gun:
    def __init__(self, g):
        self.f2_power = 10  # +power after targetting
        self.f2_on = 0  # start of fire
        self.an = 1  # angle
        self.y = 500  # starting coord of gun
        self.vx = 4  # starting speed of gun
        self.x = 20
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, fill='black', width=7)
        self.game = g

    def fire2_start(self, event):  # start of fire
        self.f2_on = 1

    def fire2_end(self, event):  # end of fire
        if self.game.continuity:
            self.game.bullet += 1
            new_ball = Ball(self.game, self.x, self.y, 9, 0, rnd(1, 5))
            self.move_gun()
            self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x + 0.00001))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = -self.f2_power * math.sin(self.an)
            self.game.balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 10

    def targetting(self):  # targetting
        x = root.winfo_pointerx() - root.winfo_rootx()
        y = root.winfo_pointery() - root.winfo_rooty()
        self.an = math.atan((y - self.y) / (x - 20 + 0.00001))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y, self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move_gun(self):
        self.x += self.vx
        if (self.x <= 10) or (self.x >= 200):
            self.vx *= -1


class Target:
    def __init__(self, type):
        self.live = 1
        self.color = 'red'
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(10, 35)
        self.vy = rnd(2, 7)
        self.vx = rnd(2, 7)
        self.type = type
        if self.type == 1:
            self.id = canv.create_oval(0, 0, 0, 0)
        elif self.type == 2:
            self.id = canv.create_rectangle(0, 0, 0, 0)
        else:
            points = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
            self.id = canv.create_polygon(points, fill=self.color, outline="black")

    def new_target(self):
        x = self.x
        y = self.y
        color = self.color
        r = self.r
        if self.type == 1 or self.type == 2:
            canv.coords(self.id, x - r, y - r, x + r, y + r)
            canv.itemconfig(self.id, fill=color)
        elif self.type == 3:
            ang = 72 / 180 * math.pi
            b = 2 * r * math.cos((90 - 72 / 2) / 180 * math.pi)  # side
            b1 = b * math.cos(ang)
            b2 = b * math.sin(ang)
            b12 = b * math.cos(ang / 2)
            b22 = b * math.sin(ang / 2)
            ang = 54 / 180 * math.pi
            x1 = b / 2
            y1 = r * math.sin(ang)
            points = [(x - x1, y - y1), (x - b1 - x1, y + b2 - y1),
                      (x + b12 - x1 - b1, y + b2 + b22 - y1),
                      (x + b + b1 - x1, y + b2 - y1), (x + b - x1, y - y1),
                      (x - x1, y - y1)]
            self.id = canv.create_polygon(points, fill=color, outline="black")
        elif self.type == 4:
            n = self.type + 2
            sid = 2 * r * math.cos((90 - 180 / n) / 180 * math.pi)
            angl = (90 - 180 / n) / 180 * math.pi
            x1 = sid / 2
            y1 = r * math.sin(angl)
            points = [(x - x1, y - y1), (x - r, y), (x - x1, y + y1),
                      (x + x1, y + y1), (x + r, y), (x + x1, y - y1),
                      (x - x1, y - y1)]
            self.id = canv.create_polygon(points, fill=color, outline="black")

    def move_target(self):
        self.y += self.vy
        self.x += self.vx
        if (self.y <= 50 + self.r) or (self.y >= 550 - self.r):
            self.vy *= -1
        if (self.x + self.r <= 100) or (self.x + self.r >= 790):
            self.vx *= -1
        canv.move(self.id, self.vx, self.vy)


class Game:
    def __init__(self):
        self.balls = []  # storage of balls
        self.bullet = 0  # number of shots
        self.number_of_targets = rnd(3, 7)
        self.targets = [Target(rnd(1, 5)) for _ in range(self.number_of_targets)]  # storage of targets
        self.g1 = Gun(self)  # cannon
        self.continuity = 1  # if continuity = 1 at least 1 target lives, if 0 - no one
        self.points = 0
        self.id_points = canv.create_text(30, 30, text=self.points, font='40')

    def new_game(self, event=''):
        screen1 = canv.create_text(350, 200, text='', font='40')
        frases = ['Вы уничтожили ', ' целей за ', ' выстрел.', ' выстрела', ' выстрелов', 'Вы сделали ',
                  ' выстрел']
        self.balls = []
        self.bullet = 0
        self.targets = [Target(rnd(1, 5)) for _ in range(self.number_of_targets)]
        for t in self.targets:  # draw targets
            t.new_target()
        canv.bind('<Button-1>', self.g1.fire2_start)
        canv.bind('<ButtonRelease-1>', self.g1.fire2_end)
        while True:
            self.targets_lives = [self.targets[i].live for i in
                                  range(self.number_of_targets)]  # storage of target's lives
            self.continuity = 1
            self.live_checker()
            if self.continuity or self.balls:
                for t in self.targets:
                    t.move_target()
                for b in self.balls:
                    b.move()
                    for t in self.targets:
                        if b.hittest(t):
                            t.live = 0
                            canv.delete(t.id)
                            self.hit()
                if self.bullet == 1:  # text during the game
                    canv.itemconfig(screen1, text=frases[5] + str(self.bullet) + frases[6])
                elif (self.bullet % 10 >= 2) and (self.bullet % 10 <= 4):
                    canv.itemconfig(screen1, text=frases[5] + str(self.bullet) + frases[3])
                else:
                    canv.itemconfig(screen1, text=frases[5] + str(self.bullet) + frases[4])
                canv.update()
                time.sleep(0.009)
                self.g1.move_gun()
                self.g1.targetting()
                self.g1.power_up()
            else:  # text after game
                if self.bullet == 1:
                    canv.itemconfig(screen1,
                                    text="{0}{1}{2}{3}{4}".format(frases[0], str(self.number_of_targets), frases[1],
                                                                  str(self.bullet), frases[2]))
                elif (self.bullet % 10 >= 2) and (self.bullet % 10 <= 4):
                    canv.itemconfig(screen1,
                                    text="{0}{1}{2}{3}{4}".format(frases[0], str(self.number_of_targets), frases[1],
                                                                  str(self.bullet), frases[3]))
                else:
                    canv.itemconfig(screen1,
                                    text="{0}{1}{2}{3}{4}".format(frases[0], str(self.number_of_targets), frases[1],
                                                                  str(self.bullet), frases[4]))
                canv.update()
                time.sleep(2)
                break
        canv.itemconfig(screen1, text='')
        root.after(500, self.new_game)

    def live_checker(self):  # it check lives of targets
        if self.targets_lives[0] == 0:
            for i in range(1, self.number_of_targets):
                if self.targets_lives[i] == self.targets_lives[i - 1]:
                    self.continuity = 0
                else:
                    self.continuity = 1
                    break

    def hit(self):
        self.points += 1
        canv.itemconfig(self.id_points, text=self.points)


game1 = Game()
game1.new_game()
mainloop()
