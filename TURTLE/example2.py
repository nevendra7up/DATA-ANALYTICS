from turtle import *
s=getscreen()
t=Turtle()

for i in range(16):
    t.fd(100)
    t.lt(360//6)
    if t.distance(0,0)<1: 
        break
    
mainloop()

