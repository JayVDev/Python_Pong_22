from turtle import Screen, Turtle

# Variables
game_is_on = True

# Create left and right paddle
r_paddle = Paddle()
l_paddle = Paddle()

# Create Screen
# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Pong Game")
# screen.tracer(0)


# create the paddle
# paddle = Turtle("square")
# paddle.color("white")
# paddle.shapesize(stretch_len=1, stretch_wid=5,)
# paddle.penup()
# paddle.goto(350, 0)
# paddle.turtlesize(stretch_len=1, stretch_wid=5)


# Functions
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

# game
while game_is_on:
    screen.update()



# Screen listen
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
















# Screen is going to close after the user click the screen
screen.exitonclick()
