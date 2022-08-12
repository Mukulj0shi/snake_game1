#!/usr/bin/env python
"""
# This module include Creating snake using turtle module.
# Moving snake forward and changing snake direction based on the inputs from keyword.
# Function snake_body defines the snake body.
# Function move_snake_fwd responsible for moving the snake and changing its direction.
"""

from turtle import Turtle, Screen

turtle_obj = Turtle()
screen_obj = Screen()
screen_obj.screensize(canvwidth=600, canvheight=600)
screen_obj.bgcolor("black")
screen_obj.title("Snake Game")
screen_obj.listen()
is_game_on = True

#Define snake body




snake_body()

screen_obj.exitonclick()
