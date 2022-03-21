# Ryan Lugo: 3/21/22

import turtle

window = turtle.Screen()
toby = turtle.Turtle()

def move_forward():
    toby.forward(50)

def move_backward():
    toby.back(50)

def turn_left():
    toby.left(90)

def turn_right():
    toby.right(90)

window.listen()

window.onkey(move_forward, "Up")
window.onkey(move_backward,"Down")
window.onkey(turn_left,"Left")
window.onkey(turn_right,"Right")


window.mainloop()