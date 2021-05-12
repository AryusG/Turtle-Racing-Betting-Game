from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# Variables
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coord = -125
all_turtles = []

# Custom Functions
def create_turtle(color_choice, y_axis):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(f"{color_choice}")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    all_turtles.append(new_turtle)

# Code
for color in colors:
    # name = color
    create_turtle(color, y_coord)
    y_coord += 50

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
    if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You Won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You lose! The {turtle.pencolor()} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
