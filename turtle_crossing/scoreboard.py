import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("forest green")
        self.penup()
        self.goto(-300 , 280)
        self.write(f"level {self.score}" , align="center", font=FONT)
    def update_score(self):
        self.score += 1
        self.clear()  # clears the old score text
        self.write(f" level {self.score} ", align="center", font=FONT)
        
    
