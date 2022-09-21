import turtle

turtle.shape('turtle')
turtle.stamp()

def reset():
    turtle.reset()


def move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

turtle.onkey(move_up,'w')
turtle.onkey(move_down,'s')
turtle.onkey(move_right,'d')
turtle.onkey(move_left,'a')
turtle.onkey(reset,'Escape')
turtle.listen()