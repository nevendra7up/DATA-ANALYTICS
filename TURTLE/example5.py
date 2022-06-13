from turtle import * 
t=Turtle()
t.speed('fastest')
bgcolor('black')
t.color('brown')

for i in range(1,300,2):
    t.fd(i)
    t.lt(60)

mainloop()