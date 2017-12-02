
import turtle

def mysteryFunc(a, n):
    while a != 0:
        temp = a % n
        print temp
        a = a/n


def RmysteryFunc(a, n):
    if a == 0:
        return
    print a % n
    return RmysteryFunc(a/n, n)

a = 10
n = 2
mysteryFunc(a, n)
RmysteryFunc(a, n)


def draw_sierpinski(length, depth):
    if depth == 0:
        for i in range(0,3):
            next.fd(length)
            next.left(120)
    else:
        draw_sierpinski(length/2, depth-1)
        next.fd(length/2)
        draw_sierpinski(length/2, depth-1)
        next.back(length/2)
        next.left(60)
        next.fd(length/2)
        next.right(60)
        draw_sierpinski(length/2, depth-1)
        next.left(60)
        next.back(length/2)
        next.right(60)

window = turtle.Screen()
next = turtle.Turtle()
draw_sierpinski(100, 2)
window.exitonclick()

