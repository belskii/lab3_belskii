import tkinter as tk
from random import randrange as rnd, choice
import math

WIDTH = 800
HEIGHT = 600
g = 10  # g per time unit
dt = 50
cs = 1.01  # collision speedup


class Ball:
    def __init__(self):
        self.R = rnd(20, 50)
        self.x = rnd(self.R, WIDTH - self.R)
        self.y = rnd(self.R, HEIGHT - self.R)
        self.dx, self.dy = (+2, +2)
        self.color = choice(['green',
                             'blue',
                             'red',
                             'pink',
                             'white',
                             'brown'])
        self.check_inside()
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill=self.color)

    def move(self):
        global g, dt

        self.x += self.dx
        self.y += self.dy
        og = game.direction
        self.dy += g * dt * math.cos(math.pi * og / 8) / 1000
        self.dx += g * dt * math.sin(math.pi * og / 8) / 1000
        if self.x + self.R > WIDTH:
            self.dx = -self.dx - 1
        if self.x - self.R <= 0:
            self.dx = 2
        if self.y + self.R > HEIGHT:
            self.dy = - self.dy - 1
        elif self.y - self.R <= 0:
            self.dy = 2
        self.check_collision()

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def check_collision(self):
        global cs

        for ball in balls:
            if self != ball and (
                            (ball.R + self.R) ** 2 >= (ball.x - self.x) ** 2 + (ball.y - self.y) ** 2):
                self.dx = - cs * self.dx
                self.dy = - cs * self.dy

    def check_inside(self):
        for i in balls:
            while (i.R + self.R) ** 2 >= (i.x - self.x) ** 2 + (i.y - self.y) ** 2:
                self.x = rnd(self.R, WIDTH - self.R)
                self.y = rnd(self.R, HEIGHT - self.R)


def tick():
    global dt

    for ball in balls:
        ball.move()
        ball.show()
    root.after(dt, tick)


class Game:
    def __init__(self):
        self.score = 0
        self.direction = 0

    def canvas_click_handler(self, event):
        for ball in balls:
            if ball.x + ball.R >= event.x >= ball.x - ball.R and ball.y + ball.R >= event.y >= ball.y - ball.R:
                self.score += 1
        print(str(self.score))
        self.direction += 1
        self.direction = self.direction % 16

    def main(self):
        global root, canvas, balls
        root = tk.Tk()
        root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        canvas = tk.Canvas(root, bg='black')
        canvas.pack(fill=tk.BOTH, expand=1)
        canvas.bind('<Button-1>', self.canvas_click_handler)
        # balls = [Ball() for i in range(5)]
        balls = []
        for i in range(5):
            balls.append(Ball())
        tick()
        root.mainloop()


game = Game()
game.main()
