import turtle

t = turtle.Turtle()
t.shape("turtle")

size = int(input('집 크기'))

t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

t.right(30)
t.forward(size)
t.right(120)
t.forward(size)