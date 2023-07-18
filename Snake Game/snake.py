from turtle import Turtle
Starting_position=[(-20,0),(-40,0)]
Moving_distance=20

class Snake :
    def __init__(self) :
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self) :
        self.create_head()
        for pos in Starting_position :
            self.add_segment(pos)

    def create_head(self) :
        snake_head=Turtle(shape="turtle")
        snake_head.color("red")
        snake_head.penup()
        snake_head.goto(0,0)
        self.segment.append(snake_head)
            
    def add_segment(self,pos) :
        new_segment=Turtle(shape="circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segment.append(new_segment)
    
    def extend(self) :
        self.add_segment(self.segment[-1].position())
            
    def move(self) :
        for pos in range(len(self.segment)-1,0,-1) :
            x_cor=self.segment[pos - 1].xcor()
            y_cor=self.segment[pos - 1].ycor()
            self.segment[pos].goto(x_cor,y_cor)
        self.segment[0].forward(Moving_distance)
    
    def up(self) :
        if self.head.heading() != 270 :
            self.head.setheading(90)
    def down(self) :
        if self.head.heading() != 90 :
            self.head.setheading(270)
    def right(self) :
        if self.head.heading() != 180 :
            self.head.setheading(0)
    def left(self) :
        if self.head.heading() != 0 :
            self.head.setheading(180)

    def reset_snake(self) :
        for seg in self.segment :
            seg.goto(1000,1000)
        self.segment.clear()
    