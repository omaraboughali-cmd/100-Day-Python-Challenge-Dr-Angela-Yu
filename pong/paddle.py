import turtle
class Paddle(turtle.Turtle):
    def __init__(self , x , y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(x , y)
        self.turtlesize(5, 1)
    
    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self
                      .xcor() , new_y )

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor() , new_y)
           

        