import turtle
import paddle
import ball
import scoreboard 
import time
screen = turtle.Screen( )
screen.bgcolor("black")
screen.title("pong")
screen.setup(800 , 600)
# screen.tracer(0)
# paddle = turtle.Turtle()
# paddle.color("white")
# paddle.penup()
# paddle.setpos(350 , 0)
# paddle.turtlesize(5, 1)
# screen.tracer(1)
screen.tracer(0)
paddle1 = paddle.Paddle(350 , 0)


ai_paddle = paddle.Paddle(-350 , 0)
scoreboard1 = scoreboard.scoreboard(-100 , 260)
dash = turtle.Turtle()
dash.penup()
dash.hideturtle()
dash.setpos(0, 260)
dash.color("white")
dash.write("***** " , align="center", font=("Consolas", 30, "bold"))
scoreboard2 = scoreboard.scoreboard(100, 260)


ball1 = ball.Ball()

game_is_on = True    
screen.listen()
screen.onkeypress(paddle1.up ,"Up")
screen.listen()
screen.onkeypress(paddle1.down ,"Down")
 
while game_is_on :  
    ball1.move()
# 1. Only react if the ball is moving toward the AI (left side)
    # Only track if the ball is moving left AND has crossed into the left half of the screen
    if ball1.x_move < 0 and ball1.xcor() < 0: 
        ai_paddle_y = ai_paddle.ycor()
        ball_y = ball1.ycor()
    
        if ai_paddle_y < ball_y - 15:
            ai_paddle.sety(ai_paddle_y + 8)
        elif ai_paddle_y > ball_y + 15:
            ai_paddle.sety(ai_paddle_y - 8)

# --- RIGHT PADDLE COLLISION (paddle1) ---
# Checks if the ball is past the paddle's X line AND within its vertical height
    if ball1.xcor() > 340: 
        if ball1.ycor() < paddle1.ycor() + 50 and ball1.ycor() > paddle1.ycor() - 50:
            ball1.setx(340)          # Prevent the ball from getting stuck inside the paddle
            ball1.x_move *= -1

# --- LEFT PADDLE COLLISION (ai_paddle) ---
    if ball1.xcor() < -340:
        if ball1.ycor() < ai_paddle.ycor() + 50 and ball1.ycor() > ai_paddle.ycor() - 50:
            ball1.setx(-340)         # Prevent the ball from getting stuck inside the paddle
            ball1.x_move *= -1     
       

    if ball1.xcor() < -390:
        scoreboard2.update_score()
        
        
    if ball1.xcor() > 390:
        
        scoreboard1.update_score()
        
        



    
    # 4. Handle collisions (Ball hitting walls or paddles)

    # 5. Refresh/Draw everything on the screen
    screen.update()
    time.sleep(0.03)
screen.exitonclick()