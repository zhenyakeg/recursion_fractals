__author__ = 'student'
import turtle as t
import time
t.speed(10)
def Koch(n,l):
    if n == 0:
        t.forward(l)
        return
    Koch(n-1,l//3)
    t.left(60)
    Koch(n-1,l//3)
    t.right(120)
    Koch(n-1,l//3)
    t.left(60)
    Koch(n-1,l//3)
def Snowflake(n,l):
    t.left(60)
    for i in range (3):
        Koch(n,l)
        t.right(120)
t.penup()
t.goto(-300,0)
t.pendown()
Snowflake(2,200)
time.sleep(5)