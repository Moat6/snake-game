from turtle import Turtle
import random

class Food(Turtle) :
    def __init__(self) :
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.refresh_food()

    def refresh_food(self) :
        random_x=random.randrange(-280,280)
        random_y=random.randrange(-280,280)
        self.goto(random_x,random_y)