import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()

screen.tracer(0)
turtle1 = Player()
score = Scoreboard()
cars = CarManager()

game_is_on = True
screen.listen()
screen.onkeypress(turtle1.up , "Up")


while game_is_on:
    cars.remove_car()
    if turtle1.finish():
        score.update_score()
        cars.level_up()
    cars.move()    
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 3) == 1:
        cars.new_car()
    
    for car in cars.list_of_cars:
            if turtle1.distance(car) < 30:
                print("game over")
                game_is_on = False 
screen.exitonclick()