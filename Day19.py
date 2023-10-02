#excercise 1: Event listener

# from turtle import Turtle,Screen

# timmy = Turtle()
# screen = Screen()

# def move_forward():
#     timmy.forward(10)

# screen.listen()
# screen.onkey(key="space",fun=move_forward)

# screen.exitonclick()

#excercise 2: Make an etch-a-sketch app

# from turtle import Turtle,Screen
# timmy = Turtle()
# screen = Screen()

# def move_forward():
#     timmy.forward(10)

# def move_backward():
#     timmy.backward(10)

# def move_right():
#     timmy.right(10)

# def move_left():
#     timmy.left(10)

# def clear_screen():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()

# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=move_backward)
# screen.onkey(key="a",fun=move_right)
# screen.onkey(key="d",fun=move_left)
# screen.onkey(key="c",fun=clear_screen)

# screen.exitonclick()

#excercise 3: Build a turtle race

from  turtle import Turtle,Screen
import random 

is_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_input = screen.textinput(title = "Make your Bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
x=-230
y=-100

for color in colors:
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y = y + 40
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")    
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()