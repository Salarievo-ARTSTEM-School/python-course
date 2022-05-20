from turtle import *
from turtle import Turtle, Screen

def drag(x, y):
   

    t1.ondrag(None)
    t1.setheading(t1.towards(x, y))
    t1.goto(x, y)
    t1.ondrag(drag)
    t2.goto((t2.xcor()*9./10+t1.xcor()*1./10),(t2.ycor()*9./10+t1.ycor()*1./10))
    update()

ws = Screen()

t1 = Turtle('turtle')
t1.speed(0)

t2=Turtle()
t2.color('red')
t2.speed(0)
t2.fd(100)
def main():
    listen() 
    t1.ondrag(drag)
    update()

main()
ws.mainloop()
