"""
Juego: Paint

Programador 1: Iván Santiago Hernández Mendoza - A01662556
Programador 2: Diego Jacobo Martínez - A01656583 

Fecha 09 / 05 / 2022

"""

from turtle import *

from freegames import vector


def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(36):             # Se repite el ciclo 36 veces, generando 36 segmentos aproximandonos así a lo que es la circunferencia
        forward(end.x - start.x)        # Marcamos la distancia que se avanza, siendo la diferencia entre los 2 puntos propuestos por el usuario
        left(10)                        # Cada vez que termina de dibujar un segmento gira 10° a la izquierda y repite el proceso

    end_fill()


def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):              # Se modifico el ciclo para que ahora solo se repita dos veces
        forward(end.x/2 - start.x/2)    # Pero ahora cuando gira en esta linea lo hace a la mitad de la distancia
        left(90)
        forward(end.x - start.x)        # Aqui mantiene la distancia y por eso se convierte en un rectangulo
        left(90)

    end_fill()


def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):          # Se modifico el ciclo para que se repita 3 veces
        forward(end.x - start.x)    # Se mantiene la longitud del trazo
        left(120)                   # Gira un total de 120 grados en sentido antihorario

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

# Implementación de distintos colores 

onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')

# Implementación de distintas formas

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
