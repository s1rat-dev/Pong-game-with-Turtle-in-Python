from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import scoreBoard

screen = Screen()
screen.setup(width=800,height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(False)

# creating necessary items with classes.
ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
score = scoreBoard()

screen.listen()
#Screen event for 1st player.
screen.onkey(r_paddle.goUp , 'Up')
screen.onkey(r_paddle.goDown, 'Down')
#Screen event for 2nd player.
screen.onkey(l_paddle.goUp , 'w')
screen.onkey(l_paddle.goDown, 's')

game_ison = True
while game_ison:
    ball.move()
    sleep(ball.speed)
    screen.update()

    #Bouncing from the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Bouncing from the paddles
    '''
        we set the distance value as 50 because the paddle can touch with top and bottom parts.
        And we blocked any error about the distance that center value as less 50 by checking the ball's x coordinate.
    '''
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320) or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    #Reset game and up to score.
    if ball.xcor() > 340:
        score.upLeftScore()
        ball.resetPosition()

    if ball.xcor() < -340:
        score.upRightScore()
        ball.resetPosition()

screen.exitonclick()