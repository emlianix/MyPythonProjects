from turtle import *
from math import cos, sin, radians

setup(1050, 400)
speed(0)
hideturtle()

def planet(x, r, color, name):
    # круг
    up()
    goto(x, -r)
    down()
    fillcolor(color)
    begin_fill()
    circle(r)
    end_fill()
    # подпись под планетой
    up()
    goto(x, -r - 25)
    write(name, align="center", font=("Arial", 10, "normal"))

planet(-401, 93, "#ffff8d", "Солнце")
planet(-255, 21, "#e3b95a", "Меркурий")
planet(-174, 28, "#e3b95a", "Венера")
planet(-104, 20, "#a0f5d0", "Земля")
planet(-46, 16, "#ff8a65", "Марс")
planet(44, 55, "#e3b95a", "Юпитер")
planet(187, 55, "#e3b95a", "Сатурн")
planet(311, 42, "#73c6dc", "Уран")
planet(405, 33, "#1a6cf0", "Нептун")
planet(477, 11, "#e3b95a", "Плутон")

# кольцо Сатурна (эллипс)
up()
goto(187 + 72, 0)
down()
for a in range(361):
    goto(187 + 72 * cos(radians(a)), 43 * sin(radians(a)))

done()