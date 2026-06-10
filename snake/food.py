import turtle
import random
class food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.tracer(0)
        self.shape("circle")
        self.speed("fastest")
        self.color("blue")
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-230, 230))
        turtle.update()
        