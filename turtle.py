import turtle 
import random
jimmy = turtle.Turtle()
jimmy.shape("circle")
jimmy.color("light blue")
colors = ["light blue", "blue", "red", "orange", "yellow", "green", "purple", "pink"]
jimmy.pensize(10)
jimmy.speed("fastest")
i = 0
jimmy.setheading(225)
jimmy.penup()
jimmy.forward(300)
jimmy.setheading(0)
def row():
    for i in range (10):
        jimmy.dot(20 , random.choice(colors))
        jimmy.forward(50)
def turn_left():
    jimmy.setheading(90)
    jimmy.forward(50)
    jimmy.setheading(180)
    jimmy.forward(50)    
def turn_right():
    jimmy.setheading(90)
    jimmy.forward(50)
    jimmy.setheading(0)
    jimmy.forward(50)

for i in range (4):
    row()
    turn_left()
    row()
    turn_right()
jimmy.hideturtle()
screen = turtle.Screen()
screen.exitonclick()