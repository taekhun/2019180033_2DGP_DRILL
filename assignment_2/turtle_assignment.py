import turtle
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

count = 1
while(count < 5):
    turtle.forward(500)
    turtle.left(90)
    count += 1

turtle.left(90)

count = 1
while(count < 5):
    turtle.goto(count * 100 - 300, -300)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    count += 1
    
turtle.right(90)

count = 1
while(count < 5):
    turtle.goto(-300, count * 100 - 300)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    count += 1
