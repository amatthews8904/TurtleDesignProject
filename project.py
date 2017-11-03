import turtle
turtle.colormode(255)
bob=turtle.Turtle()
bob.width(2)
bob.speed(2)
c=(255,0,0)
turtle.color(0,0,0)
bob.speed(11)
for times in range(256):
    bob.color(times,0,255-times)
    bob.circle(100-times)
    bob.forward(10)
    bob.left(5)
for times in range(160):
    bob.color(times,0,255,-times)
    bob.circle(100-times)
    bob.forward(250)
    bob.left(250)


import turtle
turtle.colornode(255)
bob=turtle.Turtle()
bob.width(1)
bob.speed(1)
c=(255,0,0)
turtle.color(0,0,0)
bob.speed(5)
for times in range(50):
    bob.color(times,0,255,-times)
    bob.circle(100-times)
    bob.forward(10)
    bob.right(90)
