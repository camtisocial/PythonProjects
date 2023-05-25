from turtle import Turtle, Screen
from math import pi, sqrt

#-------- variables---------#

#for iso triangles
scale = 20
a = 1+sqrt(5)
b = 2
gratio = a/b
baseGnomonScale = a*scale


#-------- screen setup ---------#
screen = Screen()
screen.setup(width = 1000, height = 1000)
screen.bgcolor("black")

#-------- pen setup ---------#
turtle = Turtle()
turtle.radians()
turtle.showturtle
turtle.color("white")


def triangleFib(iterations, turtle):
    #positioning turtle
    turtle.penup()
    turtle.setpos(-120.0, 100.0)
    turtle.pendown()

    #drawing initial triangle
    goldTriangle(turtle)

    #drawing gnomons
    for _ in range (iterations):
        goldGnomon(turtle)

    
def goldTriangle(turtle):
    turtle.fd(b*scale)
    turtle.left(3*pi/5)
    turtle.fd(a*scale)
    turtle.left(4*pi/5)
    turtle.fd(a*scale)
    turtle.left(pi)
    turtle.fd(a*scale)
    turtle.left(pi/5)

def goldGnomon(turtle):
    global baseGnomonScale
    baseGnomonScale*=gratio
    turtle.right(4*pi/5)
    turtle.fd(baseGnomonScale)
    turtle.right(4*pi/5)
    turtle.fd(baseGnomonScale/gratio)
    turtle.right(pi)
    turtle.fd(baseGnomonScale/gratio)

def main():
    triangleFib(5, turtle)

main()





screen.exitonclick()
