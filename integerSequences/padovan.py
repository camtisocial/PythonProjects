from turtle import Turtle, Screen
from math import pi, sqrt

#-------- variables---------#
#shared variable for initial values P(0) = P(1) = P(2) = 1
initVal = 1
upperRange = 13
scale = 30

#-------- screen setup ---------#
screen = Screen()
screen.setup(width = 1000, height = 1100)
screen.bgcolor("black")

#-------- pen setup ---------#
turtle = Turtle()
turtle.radians()
turtle.showturtle
turtle.color("white")
turtle.pensize(2)

def resetPen(turtle):
    turtle.penup()
    turtle.setpos(-150, -190)
    turtle.pendown()

#Recurrence relation: P(n) = P(n-2) + P(n-3)
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, etc...
def returnPadovan(upper):
    padArray=[initVal]*3 
    for i in range(3, upper):
        pn = padArray[i-2]+padArray[i-3] 
        padArray.append(pn)
    return padArray

def drawTriangle(turtle, n):
    for _ in range(4):
        turtle.fd(n)
        turtle.left(2*pi/3)
    turtle.right(pi/3)

def drawSequence(turtle, seq):
    turtle.left(2*pi/3)
    for i in range(len(seq)):
        drawTriangle(turtle, seq[i]*scale)
       
def main():
    sequence = returnPadovan(upperRange)
    resetPen(turtle)
    drawSequence(turtle, sequence)

main()


screen.exitonclick()
