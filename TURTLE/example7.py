from turtle import *
colors=['purple','green','blue','red']

pencolor(colors[0])
penup()
goto(-200,150)
pendown()
fillcolor('purple')
begin_fill()
for i in range(4):
    fd(50)
    lt(90)
end_fill()

pencolor(colors[1])
penup()
goto(200,150)
fillcolor('green')
begin_fill()
pendown()
for i in range(4):
    fd(50)
    lt(90)
end_fill()

pencolor(colors[2])
penup()
goto(-200,-150)
pendown()
fillcolor('blue')
begin_fill()
for i in range(4):
    fd(50)
    lt(90)
end_fill()


pencolor(colors[3])
penup()
goto(200,-150)
pendown()
fillcolor('red')
begin_fill()
for i in range(4):
    fd(50)
    lt(90)
end_fill()
mainloop()