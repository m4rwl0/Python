from turtle import *

diameter = 100
pop_diameter = 1000


# draws the balloon on screen
def draw_balloon():
    color("red")
    dot(diameter)


# called when we press the Up arrow key
def inflate_balloon():
    global diameter
    diameter = diameter + 100
    draw_balloon()

    # are we ready to pop?
    if diameter >= pop_diameter:
        clear()
        diameter = 1000
        write("POP!")


draw_balloon()

# call inflate_balloon when we press the Up arrow key
Screen().onkey(inflate_balloon, "Up")

Screen().listen()

# Screen() is required before onkey and listen due to the way trinket compiles the code.
# Screen() accesses the screen property, then inside of that we access the onkey and listen functions.


done()
