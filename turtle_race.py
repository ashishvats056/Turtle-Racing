from turtle import Turtle, Screen
import random


def create_turtle(color, y):
    james = Turtle(shape="turtle")
    james.color(color)
    james.penup()
    james.goto(-225, y)
    return james


if __name__ == "__main__":
    is_race_on = False
    screen = Screen()
    screen.setup(height=400, width=500)
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.setposition(230, 190)
    tim.pendown()
    tim.right(90)
    tim.forward(380)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_coordinates = [-100, -60, -20, 20, 60, 100]
    turtles = []

    for index in range(6):
        turtles.append(create_turtle(colors[index], y_coordinates[index]))

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    if user_bet in colors:
        is_race_on = True
    else:
        screen.bye()

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 215:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            distance = random.randint(0, 10)
            turtle.forward(distance)

    screen.exitonclick()
