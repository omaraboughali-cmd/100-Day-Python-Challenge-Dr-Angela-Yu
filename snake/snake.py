import turtle 
import time
import random
import scoreboard

starting_positions = [(0,0),(-20,0),(-40,0)]


class snake:

    def __init__(self , screen):
        self.segments = []
        screen.tracer(0)
        for position in starting_positions:
            turtle.tracer(0)
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.shapesize(1.5)
            new_segment.color("light blue")
            new_segment.penup()
            new_segment.goto(position) 
            self.segments.append(new_segment)
        screen.update()
    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)    
    def move(self, screen, food, scoreboard):
        game_is_on = True
        add_segment = False
    
        while game_is_on:
            time.sleep(0.1)
        
            if add_segment:
                screen.tracer(0)
                new_segment = turtle.Turtle()
                new_segment.shape("square")
                new_segment.shapesize(1.5)
                new_segment.color("light blue")
                new_segment.penup()
                new_segment.goto(self.segments[-1].position())
                self.segments.append(new_segment)
                add_segment = False

            positions = [(seg.xcor(), seg.ycor()) for seg in self.segments]
            self.segments[0].forward(20)
            for seg_num in range(1, len(self.segments)):
                self.segments[seg_num].goto(positions[seg_num - 1])

            for segment in self.segments[1:]:
                if self.segments[0].distance(segment) < 10:
                    print("game over")
                    game_is_on = False
            if self.segments[0].xcor() > 350 or self.segments[0].xcor() < -350:
                print("game over")
                game_is_on = False
            elif self.segments[0].ycor() > 300 or self.segments[0].ycor() < -300:
                print("game over")
                game_is_on = False

            if self.segments[0].distance(food) < 15:
                scoreboard.update_score()
                food.goto(random.randint(-280, 280), random.randint(-230, 230))
                add_segment = True

            screen.update()