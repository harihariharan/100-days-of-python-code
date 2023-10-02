import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Turtle()
timmy.hideturtle()
player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            timmy.write("GAME OVER", align="center", font = ("Courier", 24, "normal")) 

    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()