from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Screen setup
screen = Screen()
screen.setup(600, 600)  # Screen size: 600x600
screen.bgcolor("black")
screen.title("SNAKE GAME 🐍")
screen.tracer(0)

# Game objects
snake = Snake()
food = Food()
score = Scoreboard()

# Screen event listeners
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # Adjusted for smoother pacing
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with walls (corrected boundary check)
    # Change: Adjusted from 290 to account for the snake's full size (20x20)
    if (snake.segments[0].xcor() >= 290 or
        snake.segments[0].xcor() <= -295 or
        snake.segments[0].ycor() >= 295 or
        snake.segments[0].ycor() <= -290):
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    # No changes needed, logic is correct
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
