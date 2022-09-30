import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect if the turtle collides with the cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if the player reached the finish line
    if player.ycor() > 280:
        player.level_up()
        car_manager.move_increment()
        scoreboard.score_increase()


screen.exitonclick()
