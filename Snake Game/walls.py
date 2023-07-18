from turtle import Turtle

class Walls :
    def __init__(self) :
        self.bricks=[]
        self.create_walls()
    
    def create_brick(self) : 
        brick=Turtle("square")
        brick.color("red")
        brick.penup()
        self.bricks.append(brick)
    
    def create_walls(self) :
        x_up=-290
        for i in range(30) :
            self.create_brick()
            self.bricks[-1].goto(x_up,290)
            self.create_brick()
            self.bricks[-1].goto(x_up,-290)
            x_up += 20
        y_up=290
        for i in range(30) :
            self.create_brick()
            self.bricks[-1].goto(290,y_up)
            self.create_brick()
            self.bricks[-1].goto(-290,y_up)
            y_up -= 20
            