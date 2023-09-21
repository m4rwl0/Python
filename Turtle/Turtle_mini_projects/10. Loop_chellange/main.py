from turtle import *


def move_turtle(angle):
    x = 0
    for x in range(10):
        forward(50)
        right(angle)


move_turtle(45)

done()
