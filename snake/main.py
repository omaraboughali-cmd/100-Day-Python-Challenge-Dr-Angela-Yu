from snake import snake
import turtle  
import food
import scoreboard
screen = turtle.Screen()
s = snake(screen)
f = food.food()
sb = scoreboard.scoreboard()
screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")
s.move(screen , f , sb)


screen.exitonclick()










