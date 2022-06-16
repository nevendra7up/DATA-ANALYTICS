from turtle import * 
s=getscreen()
t=Turtle()

for i in range(8):
    t.fd(200)
    t.lt(90)
    if t.distance(0,0)<1: 
        break
        
mainloop()
