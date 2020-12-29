from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)

# Turn turtle animation off (0)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_level = screen.textinput("Choose level", "Choose game level. Type (easy/medium/hard): ")

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    # Perform a TurtleScreen update every 0.1 seconds. To be used when tracer is turned off.
    if game_level == "hard":
        sleep(0.06)
    elif game_level == "medium":
        sleep(0.08)
    else:
        sleep(0.09)

    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset_scoreboard()
        snake.reset()

    # Detect collision with tail
    for snake_part in snake.snake_parts[1:]:
        if snake.head.distance(snake_part) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()

screen.exitonclick()
