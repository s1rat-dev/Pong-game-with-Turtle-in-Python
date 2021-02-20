from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def goUp(self):
        xcor = self.xcor()
        ycor = self.ycor()
        new_position = (xcor, ycor + 20)
        self.goto(new_position)

    def goDown(self):
        xcor = self.xcor()
        ycor = self.ycor()
        new_position = (xcor, ycor - 20)
        self.goto(new_position)
