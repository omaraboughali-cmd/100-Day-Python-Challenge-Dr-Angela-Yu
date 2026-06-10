import turtle
class scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("light blue")
        self.write(f"Score is {self.score} ", align="center", font=("Arial", 16, "normal"))
    def update_score(self):
        self.score += 1
        self.clear()  # clears the old score text
        self.write(f"Score is {self.score} ", align="center", font=("Arial", 16, "normal"))