import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(30) :
  a = random.randint(0,100)
  b = random.randint(0,360)
  t.forward(a)
  t.right(b)