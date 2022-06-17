import turtle
import random
import math

turtle.tracer(20,0)
def create_turtles():
    global t,vx,vy,m,fx,fy,monitor
    t=[]

    vx=[];vy=[] #initial velocities
    m=[] #masses
    fx=[];fy=[] #forces
    for i in range(10):
        t.append(turtle.Turtle())
        t[-1].up() 
        t[-1].setpos(random.randrange(0,400)-200,random.randrange(0,400)-200)
        t[-1].fd(100)
        vx.append(random.randrange(-1,1))
        vy.append(random.randrange(-1,1))
        m.append(random.randrange(1,5))
        t[-1].turtlesize(m[-1],m[-1])
        fx.append(0)
        fy.append(0)
    monitor=turtle.Turtle() #extra turtle
    monitor.ht()

#def move(turtle):
def force(distance):
    const=10
    f=const/(distance**2)
    return f
def main_loop():
    while 1:
        kinenergy=0
        for k in range(len(t)):
            fx[k]=0
            fy[k]=0
            
            for j in range(len(t)):

                if j==k:
                    continue
                dkj=t[k].distance(t[j])
                fx[k]+=(t[j].xcor()-t[k].xcor())/(dkj**0.5)*force(dkj) #x-force from jth turtle
                fy[k]+=(t[j].ycor()-t[k].ycor())/(dkj**0.5)*force(dkj) #y-force from jth turtle
            vx[k]+=fx[k]/m[k] #acceleration from force
            vy[k]+=fy[k]/m[k]
            t[k].setx((t[k].xcor()+vx[k]+200)%400-200) #use periodic boundaries
            t[k].sety((t[k].ycor()+vy[k]+200)%400-200)
            
            kinenergy+=m[k]/2*(vx[k]**2+vy[k]**2) #summation of kinetic energies

            #t[k].setpos((t[k].xcor()+t[(k+2)%len(t)].xcor())/2,(t[k].ycor()+t[(k+2)%len(t)].ycor())/2)
        monitor.clear()
        monitor.write(round(kinenergy,2)) #monitor total kinetic energy
        turtle.update()

def main():
    create_turtles()
    main_loop()

main()

turtle.done()
