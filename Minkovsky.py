__author__ = 'student'
import turtle as t
import time
t.speed(10)
def Minkovsky(n,l):
    if n==0:
        t.forward(l)
    else:
        Minkovsky(n-1,l//4)
        t.left(90)
        Minkovsky(n-1,l//4)
        t.right(90)
        Minkovsky(n-1,l//4)
        t.right(90)
        Minkovsky(n-1,l//4)
        Minkovsky(n-1,l//4)
        t.left(90)
        Minkovsky(n-1,l//4)
        t.left(90)
        Minkovsky(n-1,l//4)
        t.right(90)
        Minkovsky(n-1,l//4)
t.penup()
t.goto(-400,0)
t.pendown()
Minkovsky(4,900)
