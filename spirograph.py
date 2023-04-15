import turtle
import random

alpha = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

alpha.speed("fastest")

for _ in range(1,37):
    alpha.color((random_color()))
    alpha.circle(100)
    alpha.setheading(alpha.heading() + 10)


screen1 = turtle.Screen()
screen1.exitonclick()