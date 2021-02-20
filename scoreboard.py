from turtle import Turtle

class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.writeScore()


    def writeScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 70, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 70, 'normal'))

    def upLeftScore(self):
        self.l_score += 1
        self.writeScore()

    def upRightScore(self):
        self.r_score += 1
        self.writeScore()

