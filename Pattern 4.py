import turtle

def draw_square(some_turtle):
    for i in range(1,6):
        some_turtle.forward(90)
        some_turtle.right(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

#creat the turtle brade - draw a square
    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("White")
    brad.speed(19)

    for i in range(1,37):
        draw_square(brad)
        brad.right(50)

    window.exitonclick()

draw_art()