__author__ = 'student'
import turtle as t
import time
t.speed(10)
def Levi(n,l):
    if n == 0:
        t.forward(l)
    else:
        t.left(45)
        Levi(n-1,l/(2)**0.5)
        t.right(90)
        Levi(n-1,l/(2)**0.5)
        t.left(45)
# t.penup()
# t.goto(-300,0)
#t.pendown()
Levi(10,400)
time.sleep(5)