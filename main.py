import turtle
from random import choice

alpha = turtle.Turtle()

alpha.speed("slow")
alpha.forward(200)
alpha.shape("turtle")
alpha.color("lawngreen")
alpha.left(90)
alpha.forward(200)
alpha.color("yellow")
alpha.left(90)
alpha.forward(200)
alpha.stamp()
alpha.color("red")
alpha.left(90)
alpha.forward(200)

turtle.clearscreen()

alpha.penup()
alpha.setx(250)
alpha.sety(250)
alpha.pendown()

alpha.speed("fast")
for _ in range(1,11):
    alpha.pendown()
    alpha.forward(10)
    alpha.penup()
    alpha.forward(10)


turtle.clearscreen()

alpha.speed("slow")
alpha.setx(0)
alpha.sety(0)
alpha.pendown()
colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
alpha.shape("turtle")
for n in range (1,10):
   alpha.color(choice(colours))
   for _ in range(1,n+1):
       alpha.forward(100)
       alpha.left(360/n)

hello = turtle.getshapes()

turtle.clearscreen()

alpha.speed("fastest")
alpha.pensize(10)
for _ in range(1,201):
   alpha.color(choice(colours))
   directions = [0,90,180,270]
   alpha.forward(30)
   alpha.setheading(choice(directions))


screen = turtle.Screen()
screen.exitonclick()

print(hello)
