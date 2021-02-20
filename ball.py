from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.goto(0,0)
        self.move_y = 10
        self.move_x = 10
        self.speed = 0.1

    def move(self):
        new_position = (self.xcor() + self.move_x, self.ycor() + self.move_y)
        self.goto(new_position)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.speed *= 0.9


    def resetPosition(self):
        self.goto(0,0)
        self.bounce_x()
        self.speed = 0.1