from turtle import *
import turtle
from turtle import Screen, Turtle

ws = Screen()
tur = turtle.Turtle()
tur.speed(0)
turtle.tracer(0,0)

def dragging(x, y): 
    tur.ondrag(None)
    tur.setheading(tur.towards(x, y))
    tur.goto(x, y)
    tur.ondrag(dragging)
    turtle.update()

def clear():
    tur.clear()
    turtle.update()

def main():  
    turtle.listen()
    
    tur.ondrag(dragging)  
    turtle.onscreenclick(clear, 2)
    turtle.onkey(clear,'c')
    turtle.update()
    ws.mainloop()  

main()
