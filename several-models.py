import turtle
import random
t=[]
for i in range(10):
    t.append(turtle.Turtle())
    #t[-1].up()
    t[-1].lt(random.randrange(0,360))
    t[-1].fd(300)

while 1:
    for k in range(len(t)):
        t[k].setpos((t[k].xcor()+t[(k+2)%len(t)].xcor())/2,(t[k].ycor()+t[(k+2)%len(t)].ycor())/2)


turtle.done()