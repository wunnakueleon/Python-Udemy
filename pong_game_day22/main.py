from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import random

dx = 0
dy = 0


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Ping")

right_paddle = Paddle()
right_paddle.paddle_position("right")

left_paddle = Paddle()
left_paddle.paddle_position("left")

# Paddles show up on screen
right_paddle.paddle.showturtle()
left_paddle.paddle.showturtle()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

ball = Ball()
position = (dx, dy)

game_is_on = True
x_cor = 0
y_cor = 0
dx = random.randint(1, 15)
dy = random.randint(1, 15)


while game_is_on:

    if y_cor >= 280 or y_cor <= -280:
        dy *= -1

    if x_cor >= 350 or x_cor <= -350:
        right_paddle.paddle.hideturtle()
        left_paddle.paddle.hideturtle()
        ball.hideturtle()
        print("Game Over Mann")
        game_is_on = False

    if right_paddle.paddle.distance(x_cor, y_cor) <= 30 or left_paddle.paddle.distance(x_cor, y_cor) <= 30:
        dx *= -1
        

    x_cor += dx
    y_cor += dy


    ball.bounce((x_cor, y_cor))

    

screen.exitonclick()


