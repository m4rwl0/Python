from random import *
from turtle import *

random_number = randrange(1, 10)
print(random_number)


def turtle_move():
    forward(randrange(20, 100))
    right(randrange(0, 360))
    forward(randrange(20, 100))


Screen().onkey(turtle_move, "Up")

Screen().listen()

done()
