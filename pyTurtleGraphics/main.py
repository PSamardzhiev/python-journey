# import modules to demonstrate OOP
# meet my crazy turtle timmy, run the below code and observe the behaviour

from turtle import Turtle, Screen
from random import random
my_screen = Screen()
my_screen.title("Python OOP Concepts Demo")
my_screen.bgcolor("orange")

timmy = Turtle()
timmy.color("purple")
timmy.shape("turtle")
timmy.shapesize(2)
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 180)
    timmy.right(angle)
    timmy.fd(steps)




