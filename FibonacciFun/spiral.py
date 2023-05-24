from turtle import Turtle, Screen
from math import pi, sqrt

#-------- screen setup ---------#
scale = 50
screen = Screen()
screen.setup(width = 1000, height = 1000)
screen.bgcolor("black")

#-------- pen setup ---------#
turtle = Turtle()
turtle.radians()
turtle.showturtle
turtle.color("white")


def triangleFib(iterations, turtle):
    turtle.penup()
    turtle.setpos(-100.0, 0.0)
    turtle.pendown()

    goldTriangle(turtle)

    




def goldTriangle(turtle):
    a = scale*(1+sqrt(5));
    b = scale*2

    turtle.fd(b);
    turtle.left(3*pi/5)
    turtle.fd(a);
    turtle.left(4*pi/5)
    turtle.fd(a);
    turtle.left(pi)
    turtle.fd(a);


def main():
    triangleFib(3, turtle)

main()





screen.exitonclick()
