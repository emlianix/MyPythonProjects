from turtle import *

pensize(3)

# Walls (blue square)
fillcolor("#00a2e8")
penup()
goto(-100, -100)
pendown()
begin_fill()
for _ in range(4):
    forward(200)
    left(90)
end_fill()

# Roof (brown triangle, wider than the walls)
fillcolor("#b87b58")
penup()
goto(-145, 100)
pendown()
begin_fill()
goto(145, 100)
goto(0, 282)
goto(-145, 100)
end_fill()

hideturtle()
done()