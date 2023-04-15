import turtle
import random

alpha = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


alpha.pendown()
alpha.pensize(30)
alpha.speed("fastest")
for _ in range(1,201):
   alpha.color((random_color()))
   directions = [0,90,180,270]
   alpha.forward(30)
   alpha.setheading(random.choice(directions))

screen1 = turtle.Screen()
screen1.exitonclick()