
import turtle


class Auto(turtle.Turtle):
    def __init__(self, szin, x, y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(5)
        self.goto(x, y)
        self.sebesseg = sebesseg

    def indit(self):
        self.forward(self.sebesseg)
