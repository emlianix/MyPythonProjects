from turtle import *
from random import randint, choice
from time import sleep

SKY = "#001F44"
BUILDING = "#0443A0"
LIGHT = "#FFFF88"

# Холст: квадрат 408x408 с центром в (0, 0)
LEFT, RIGHT, BOTTOM, TOP = -204, 204, -204, 204

# Здания: (левый край, правый край, высота крыши)
buildings = [
    (-204, -150, -63),
    (-150,  -87,   8),
    ( -87,   10, 154),
    (  10,   65, -23),
    (  65,  132,  81),
    ( 132,  165,  11),
    ( 165,  204, -63),
]


def draw_rect(x, y, w, h, fill):
    """Заливает прямоугольник с левым нижним углом (x, y)."""
    penup()
    goto(x, y)
    setheading(0)
    color(fill)
    pendown()
    begin_fill()
    for side in (w, h, w, h):
        forward(side)
        left(90)
    end_fill()
    penup()


def draw_sky():
    draw_rect(LEFT, BOTTOM, RIGHT - LEFT, TOP - BOTTOM, SKY)


def draw_buildings():
    """Рисует контуры (силуэт) всех зданий."""
    for x1, x2, roof in buildings:
        draw_rect(x1, BOTTOM, x2 - x1, roof - BOTTOM, BUILDING)


def on_building(x, y):
    """True, если точка попадает на здание."""
    for x1, x2, roof in buildings:
        if x1 <= x <= x2 and y <= roof:
            return True
    return False


def draw_windows(windows, size=17, delay=0.6):
    """Рисует окна по одному; windows - список левых нижних углов."""
    for x, y in windows:
        draw_rect(x, y, size, size, LIGHT)
        update()
        sleep(delay)


def draw_stars(count=20, delay=0.25):
    """Рисует звёзды-точки по одной, только на небе."""
    drawn = 0
    while drawn < count:
        x = randint(LEFT + 5, RIGHT - 5)
        y = randint(BOTTOM + 5, TOP - 5)
        if on_building(x, y):
            continue  # звезда попала на здание - выбираем другую точку
        goto(x, y)
        dot(choice([2, 2, 3, 5]), LIGHT)
        update()
        sleep(delay)
        drawn += 1


def main():
    window_positions = [(-77, 120), (-77, 98), (-17, 44),
                        (72, 33), (-144, -25), (-54, -83)]

    setup(500, 500)
    tracer(0)
    hideturtle()
    penup()

    draw_sky()
    draw_buildings()
    update()          # сначала показываем небо и здания

    draw_windows(window_positions)  # потом по очереди появляются окна
    draw_stars(20)                  # и в конце звёзды

    done()


main()