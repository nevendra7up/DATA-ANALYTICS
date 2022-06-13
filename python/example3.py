from turtle import *
s=getscreen()
t=Turtle() 

for i in range(6):
    t.fd(100)
    t.lt(360//6)
    t.dot(20)
    t.circle(50,180)
mainloop()
