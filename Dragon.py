__author__ = 'student'
import turtle as t
import time
t.speed(10)
def Dragon(n,l,angle = 0):

        if n == 0:
            t.forward(l)
        else:
            # if angle == -1:
            #     t.left(45)
            #     Dragon(n-1,l/2**0.5, angle = -1)
            #     t.right(90)
            #     Dragon(n-1,l/2**0.5, angle = 1)
            #     t.left(45)
            #
            # elif angle == 1:
            t.right(angle*45)
            Dragon(n-1,l/2**0.5, angle= -1)
            t.left(angle*90)
            Dragon(n-1,l/2**0.5, angle= 1)
            t.right(angle*45)

Dragon(9,200)
input()