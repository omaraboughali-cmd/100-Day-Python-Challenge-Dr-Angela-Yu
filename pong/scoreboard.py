import turtle
class scoreboard(turtle.Turtle):
    def __init__(self , x , y ): 
        super().__init__()
        self.hideturtle()
        self.penup() 
        self.goto(x , y)
        self.score = 0 
        self.color("white")
        self.write(f"{self.score} ", align="center", font=("Consolas", 30, "bold"))
    def update_score(self):
        self.score += 1
        self.clear()  # clears the old score text
        self.write(f"{self.score} ", align="center", font=("Consolas", 30, "bold"))