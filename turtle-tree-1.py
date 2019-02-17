#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
用Python-turtle library 作图画出漂亮的树， 来自于《知乎》Milo Yip ： 游戏开发者优秀回答

"""


from turtle import pd, pu, circle, heading, pencolor, pensize, forward
from turtle import backward, right, left, bgcolor, ht, speed, tracer, done
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)

    pu()
    backward(l)

if __name__ == '__main__':
    bgcolor(0.5, 0.5, 0.5)
    ht()
    speed(0)
    tracer(0, 0)
    left(90)
    pu()
    backward(300)
    tree(13, 100)
    done()
