from turtle import *
s=getscreen()
speed('fastest')
color('red', 'yellow')
begin_fill()
while(True):
    fd(200)
    lt(190)
    if distance(0,0)<1:
        break

end_fill()
mainloop()