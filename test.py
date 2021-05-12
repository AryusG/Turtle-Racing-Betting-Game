from turtle import Turtle, Screen


# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#
# t = Turtle(shape="turtle")
# t.color(f"{colors[0]}")
# t.penup()
# t.goto(x=-230, y=-100)
#
#
#
# screen.exitonclick()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for color in colors:
    for i in range(0, colors.index[color]):
        print(color)
