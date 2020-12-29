import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Drawing gradient')
color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    for i in range(10)]

A = turtle.Turtle()
A.speed(0)
A.color(random.choice(color))
rotate = int(360)
def draw_circle(t, size):
    for i in range(10):
        t.circle(size)
        size -= 4
def draw_special(t, size, repeat):
    for i in range(repeat):
        draw_circle(t, size)
        t.right(360 / repeat)
draw_special(A, 100, 10)

B = turtle.Turtle()
B.speed(0)
B.color(random.choice(color))
rotate = int(90)
def draw_circle(t, size):
    for i in range(4):
        t.circle(size)
        size -= 10
def draw_special(t, size, repeat):
    for i in range(repeat):
        draw_circle(t, size)
        t.right(360 / repeat)
draw_special(B, 100, 10)

C = turtle.Turtle()
C.speed(0)
C.color(random.choice(color))
rotate = int(80)
def draw_circle(t, size):
    for i in range(4):
        t.circle(size)
        size -= 5
def draw_special(t, size, repeat):
    for i in range(repeat):
        draw_circle(t, size)
        t.right(360 / repeat)
draw_special(C, 100, 10)

D = turtle.Turtle()
D.speed(0)
D.color(random.choice(color))
rotate = int(90)
def draw_circle(t, size):
    for i in range(4):
        t.circle(size)
        size -= 19
def draw_special(t, size, repeat):
    for i in range(repeat):
        draw_circle(t, size)
        t.right(360 / repeat)
draw_special(D, 100, 10)

E = turtle.Turtle()
E.speed(0)
E.color(random.choice(color))
rotate = int(90)
def draw_circle(t, size):
    for i in range(4):
        t.circle(size)
        size -= 20
def draw_special(t, size, repeat):
    for i in range(repeat):
        draw_circle(t, size)
        t.right(360 / repeat)
draw_special(E, 100, 10)

turtle.getscreen()._root.mainloop()