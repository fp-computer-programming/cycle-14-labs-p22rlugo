# Ryan Lugo: RJL 3/18/22

import turtle

window = turtle.Screen()
window.title("Lab 4")

mark = turtle.Turtle()
mark.speed(1)
mark.color("red")
mark.pencolor("blue")
mark.stamp()
mark.begin_fill()

mark.goto(100,0)
mark.goto(100,100)
mark.goto(0,100)
mark.goto(0,0)

mark.end_fill()

window.mainloop()