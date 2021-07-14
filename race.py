from turtle import Turtle, Screen
import random


# this is false so that if user doesn't choose anything game will not start
is_race_on = False


# Setting the screen
screen = Screen()
screen.setup(width=800, height=600)

# Making choice screen
player_bet = screen.textinput(title='Welcome', prompt='Which color will win (available color are red, orange, yellow, blue, purple, green ): ')
colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
all_turtle = []

# Adjusting the y coordinate of each turtle, you are free to mess up and choose coordinate of your liking
y = 30

# Making of each turtle
for turtles in range(6):
    ghost = Turtle('turtle')
    ghost.color(colors[turtles])
    ghost.penup()

    # each turtle x-coordinate should be same (no cheating) but y coordinate should differ.
    ghost.goto(-380.0, -150.0 + y)
    y += 50

    # Appending each turtle in a list so that we can move each turtle.
    all_turtle.append(ghost)


# If player made there choice then why are we waiting game is on.
if player_bet:
    is_race_on = True

winner = None

# Game loop
while is_race_on:
    
    # making each turtle walk randomly.
    for turtles in all_turtle:
        random_walk = random.randint(1, 10)
        turtles.forward(random_walk)

        # Checking for winner with simple if condition.
        if turtles.xcor() >= 380.0:
            is_race_on = False

            # Which color turtle won
            winner = turtles.pencolor()
            if winner == player_bet:
                print('You win')
            else:
                print(f'you lose. Winner is {winner}')

screen.exitonclick()
