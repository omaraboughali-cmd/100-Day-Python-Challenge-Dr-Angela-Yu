import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()        
        self.penup()
        self.setheading(90)
        self.turtlesize(2)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.color("light green")
    
        
    def up(self):
        self.forward(MOVE_DISTANCE)    
    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.hideturtle()
            self.goto(STARTING_POSITION)
            self.showturtle()
            return True

    
