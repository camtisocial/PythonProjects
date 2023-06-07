from turtle import Turtle, Screen
from math import pi, sqrt

#-------- variables---------#
#shared variable for initial values P(0) = P(1) = P(2) = 1
initVal = 1
lowerRange = 3
upperRange = 15

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

def resetPen(turtle):
    turtle.penup()
    turtle.home()
    turtle.pendown()

#Recurrence relation: P(n) = P(n-2) + P(n-3)
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, etc...
def returnPadovan():
    padArray=[initVal]*3 
    for i in range(lowerRange, upperRange):
        Pn = padArray[i-2]+padArray[i-3] 
        padArray.append(Pn)
    return padArray
       
def main():
    sequence = returnPadovan();
    print(sequence)

main()


screen.exitonclick()
