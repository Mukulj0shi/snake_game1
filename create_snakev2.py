#!/usr/bin/env python

"""
# This is snake class.
# Create snake body by calling the Snake() class
# Move snake by calling snake_move() method.
"""

from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]    #Constant are defined at the top of the program in capital letters and snake case.
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.turt_obj_list = []                         # Here we are defining the attributes related to snake creation.
        self.create_snake()
        self.head = self.turt_obj_list[0]


    # Define snake body
    def create_snake(self):
        for cord in STARTING_POSITIONS:
            turtle_obj1 = Turtle()  # This will create 3 turtle objects.
            # Specifying object outside loop will create only single object.
            turtle_obj1.shape("square")
            turtle_obj1.color("white")
            turtle_obj1.penup()
            turtle_obj1.speed(1)
            turtle_obj1.goto(cord)
            self.turt_obj_list.append(turtle_obj1)      #Calling attributes in methods using self.attribute_name.

    def move_snake(self):
        for items in range((len(self.turt_obj_list) - 1), 0, -1):
            x_cord = self.turt_obj_list[items - 1].xcor()  # Last item moves to second last item position
            y_cord = self.turt_obj_list[items - 2].ycor()
            self.turt_obj_list[items].goto(x_cord, y_cord)
        self.head.forward(MOVE_DISTANCE)               #Calling attributes in methods using self.attribute_name.

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    #create_snake()
    #move_snake()
    #screen_obj.exitonclick()
