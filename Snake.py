import turtle
import time
import random

delay = 0.1

# Створення вікна для гри
wn = turtle.Screen()
wn.title("Гра Змійка")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Вимкнення оновлення екрану

# Голова змійки
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Їжа для змійки
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Функції
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Керування змійкою
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Основний цикл гри
while True:
    wn.update()

    # Перевірка на зіткнення з межами екрану
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Прибирання сегментів тіла
        for segment in segments:
            segment.goto(1000, 1000)

        # Очищення списку сегментів
        segments.clear()

    # Перевірка на зіткнення з їжею
    if head.distance(food) < 20:
        # Переміщення їжі випадково
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Додавання нового сегмента до тіла змійки
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Переміщення кінця тіла до переднього сегмента в зворотному порядку
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Переміщення сегменту 0 до голови
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Перевірка на зіткнення з тілом змійки
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Прибирання сегментів тіла
            for segment in segments:
                segment.goto(1000, 1000)

            # Очищення списку сегментів
            segments.clear()

    time.sleep(delay)

wn.mainloop()
