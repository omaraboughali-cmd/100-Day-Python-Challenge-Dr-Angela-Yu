import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.list_of_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def new_car(self):
        new_car = turtle.Turtle()
        new_car.hideturtle()
        new_car.penup()
        new_car.color("light blue")
        new_car.shape("square")
        new_car.shapesize(1 , 2)
        new_car.showturtle()
        y = random.randint(-280, 280)
        for car in self.list_of_cars:
            if abs(car.ycor() - y) < 20:
                new_car.hideturtle()
                return
        new_car.setpos(350,random.randint(-280 , 280))
        new_car.left(180)
        self.list_of_cars.append(new_car)
        

    def move(self):
        for car in self.list_of_cars:
            car.forward(self.speed)
    
    
    def level_up(self):
        self.speed += MOVE_INCREMENT
        print(self.speed)
    def remove_car(self):
        for car in self.list_of_cars[:]:
            if car.xcor() <= -350:
                car.hideturtle()
                self.list_of_cars.remove(car)    
        
            
