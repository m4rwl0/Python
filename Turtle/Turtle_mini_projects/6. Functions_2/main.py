from turtle import *


def move_and_turn(distance, angle):
    forward(distance)
    right(angle)
    print("turtle is moving!")


move_and_turn(100, 45)
move_and_turn(200, 90)

done()
