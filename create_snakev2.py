#!/usr/bin/env python
"""
# This module include Creating snake using turtle module.
# Moving snake forward and changing snake direction based on the inputs from keyword.
# Function snake_body defines the snake body.
# Function move_snake_fwd responsible for moving the snake and changing its direction.
"""

from turtle import Turtle, Screen

turtle_obj1 = Turtle()
turtle_obj2 = Turtle()
turtle_obj3 = Turtle()
screen_obj = Screen()
screen_obj.screensize(canvwidth=600, canvheight=600)
screen_obj.bgcolor("black")
screen_obj.title("Snake Game")
screen_obj.listen()
is_game_on = True



#Define snake body
turtle_obj1.goto(0,0)
turtle_obj1.shape("square")
turtle_obj1.fillcolor("white")


turtle_obj2.goto(-20,0)
turtle_obj2.shape("square")
turtle_obj2.fillcolor("white")


turtle_obj3.goto(-40,0)
turtle_obj3.shape("square")
turtle_obj3.fillcolor("white")




screen_obj.exitonclick()
