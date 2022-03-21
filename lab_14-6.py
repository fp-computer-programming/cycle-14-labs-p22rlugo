# Ryan Lugo: RJL 3/21/22

import turtle

color = input("Give me a random color: ")

window = turtle.Screen()
mark = turtle.Turtle()

size = turtle.numinput("Size", "How big do you want the turtle?(Min: 1, Max: 5): ", default=None, minval=None,
maxval=None)

def fill():
    mark.begin_fill()

    mark.forward(100)
    mark.left(90)
    mark.forward(100)
    mark.left(90)
    mark.forward(100)
    mark.left(90)
    mark.forward(100)

    mark.end_fill()


mark.color(color)
mark.shapesize(size)

turtle.onscreenclick(fill())

window.mainloop()

