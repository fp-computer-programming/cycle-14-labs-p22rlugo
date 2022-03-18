# Ryan Lugo: RJL 3/18/22

import turtle

window = turtle.Screen()
window.setup(500,500)
window.title("Lab 3")
window.bgcolor("grey")

mark = turtle.Turtle()
mark.shape("turtle")
mark.pencolor("blue")

mark.left(90)
mark.left(90)

for x in range(2):
    mark.forward(200)
    mark.right(90)

mark.goto(0,0)

window.mainloop()