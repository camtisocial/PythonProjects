from turtle import Turtle, Screen
from math import pi, sqrt

#-------- variables---------#

#for iso triangles
scale = 20
a = 1+sqrt(5)
b = 2
g_ratio = a/b
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
turtle.pensize(2)


def triangularSpiral(iterations, turtle):
    turtle.penup()
    turtle.home()
    turtle.setpos(-120.0+b*scale, 100.0)
    turtle.pendown()
    turtle.setheading(5.235987)
    drawArc(iterations, turtle)

def drawArc(iterations, turtle):
    turtle.color("HotPink1")
    global baseGnomonScale
    baseGnomonScale = a*scale
    angle = 4*pi/3
    turtle.right(angle)
    turtle.circle(0.36*baseGnomonScale, -2*pi/3)
    baseGnomonScale*=g_ratio
    angle*=1.475

    for _ in range (iterations):
        turtle.right(angle)
        turtle.circle(0.35*baseGnomonScale, -2*pi/3)
        baseGnomonScale*=g_ratio*1.039


def triangleFib(iterations, turtle):
    resetPen(turtle)
    goldTriangle(turtle)
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
    baseGnomonScale*=g_ratio
    turtle.right(4*pi/5)
    turtle.fd(baseGnomonScale)
    turtle.right(4*pi/5)
    turtle.fd(baseGnomonScale/g_ratio)
    turtle.right(pi)
    turtle.fd(baseGnomonScale/g_ratio)

def resetPen(turtle):
    turtle.penup()
    turtle.home()
    turtle.setpos(-120.0, 100.0)
    turtle.pendown()

def main():
    triangleFib(5, turtle)
    triangularSpiral(6, turtle)

main()



screen.exitonclick()
