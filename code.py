"""Snake, classic arcade game.
CAMBIO DE COLOR + COMIDA EN MOVIMIENTO ALEATORIO
Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# CAMBIO: lista de colores disponibles (sin rojo)
colors = ['blue', 'green', 'purple', 'orange', 'brown']

# CAMBIO: elegir colores distintos al inicio
snake_color = choice(colors)
food_color = choice([c for c in colors if c != snake_color])

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(point):
    """Return True if point inside boundaries."""
    return -200 < point.x < 190 and -200 < point.y < 190


def move_food():
    """Mueve la comida un paso aleatorio sin salirse de la ventana."""
    from random import choice
    step = choice([vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)])
    new = food + step
    if inside(new):
        food.move(step)
    # si el movimiento la sacaría de la ventana, se queda en su lugar


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        # Mueve la comida a una nueva posición aleatoria al ser comida
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # --- NUEVO: mover la comida aleatoriamente en cada frame ---
    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


# --- Configuración inicial ---
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# --- Controles de dirección ---
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
