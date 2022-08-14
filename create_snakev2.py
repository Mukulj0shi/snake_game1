#!/usr/bin/env python

"""
# This module include Creating snake using turtle module.
# Moving snake forward and changing snake direction based on the inputs from keyword.
# Function snake_body defines the snake body.
# Function move_snake_fwd responsible for moving the snake and changing its direction.
"""

from turtle import Turtle, Screen
import time

# turtle_obj1 = Turtle()
screen_obj = Screen()
screen_obj.tracer(0)
screen_obj.screensize(canvwidth=600, canvheight=600)
screen_obj.bgcolor("black")
screen_obj.title("Snake Game")  # Represent title of the screen.
screen_obj.listen()

is_game_on = True
snake_cord = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
turt_obj_list = []

# Define snake body
def create_snake():
    for cord in snake_cord:
        turtle_obj1 = Turtle()  # This will create 3 turtle objects.
        # Specifying object outside loop will create only single object.
        turtle_obj1.shape("square")
        turtle_obj1.color("white")
        turtle_obj1.penup()
        turtle_obj1.speed(1)
        turtle_obj1.goto(cord)
        turt_obj_list.append(turtle_obj1)

def move_snake():
    while is_game_on:
        for items in range((len(turt_obj_list)-1), 0, -1):
            x_cord = turt_obj_list[items - 1].xcor()         #Last item moves to second last item position
            y_cord = turt_obj_list[items - 2].ycor()
            turt_obj_list[items].goto(x_cord, y_cord)
        turt_obj_list[0].forward(20)
        time.sleep(1)
        #turt_obj_list[0].left(90)
        screen_obj.update()









screen_obj.exitonclick()
