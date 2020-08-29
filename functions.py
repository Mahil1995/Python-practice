import turtle


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


import math


def polyline(t, length, n, angle):
    """" now to add angle to the polygon function, naming the function polyline as it no longer may make a polygon"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def r_polyline(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)


def polygon(t, n, length):
    angle = 360 / n
    polyline(t, length, n, angle)


def arc(t, r, angle):
    arc_circumference = 2 * math.pi * r * angle / 360
    n = int(arc_circumference / 3) + 1
    step_length = arc_circumference / n
    step_angle = float(angle / n)
    polyline(t, step_length, n, step_angle)


def circle(t, r):
    arc(t, r, 360)


def flower(t, r, angle):
    n = int(360 / angle)
    for i in range(n):
        petal(t, r, angle)


def petal(t, r, angle):
    arc(t, r, angle)
    t.lt(180 - angle)
    arc(t, r, angle)
    t.lt(180)


def n_layer_flower(t, r, angle, n):
    for i in range(n):
        flower(t, r, angle)
        t.lt(angle / 2)


def eq_triangle(t,length):
    t.fd(length)
    t.lt(180 - 60)
    t.fd(length)
    t.lt(180 - 60)
    t.fd(length)

def turtle_pie_eq(t,length):
        "equalateral triangles making a pie"
        n=int(360/60)
        t.lt(30)
        for i in range(n):
                eq_triangle(t,length)
                t.lt(180)


def right_angle_triangle(t, a_length, b_length):
    hypotenuse = float(math.sqrt(a_length ** 2 + b_length ** 2))
    a_angle = math.degrees(math.asin(a_length/hypotenuse))
    b_angle = math.degrees(math.asin(b_length/hypotenuse))
    c_angle = 90

    t.fd(a_length)
    t.lt(180 - b_angle)
    t.fd(hypotenuse)
    t.lt(180-a_angle)
    t.fd(b_length)
    t.lt(c_angle)

def triangle_loop(t,a_length,b_length,angle):
        n = int(360/angle)
        for i in range(n):
                right_angle_triangle(t,a_length,b_length)
                t.lt(angle)

def isc_triangle(t,x,B):
        "this function uses the rules of a right angle triangle to create an iscoscles triangle"
        "definitely made a mistake here, check later if you want"
        d = math.sin(B) * x
        c = math.cos(B) * x
        x = math.sqrt(c**2+d**2)
        A = math.degrees(math.acos(d/x))

        t.fd(c)
        t.lt(90)
        t.fd(d)
        t.lt(180-A)
        t.fd(x)
        t.lt(180-B)
        t.fd(c)

        print(d)
        print(c)
        print(x)
        print(B)
        print(A)

def triangular_polygon(turtle, length, n):
    "length / (2 * math.sin(math.pi / n))"
    inside_angle = (math.pi-(2*math.pi/n))/2
    rotating_angle = math.pi - inside_angle
    radius = length / (2 * math.sin(math.pi / n))


    print(inside_angle*180/math.pi)
    print(rotating_angle*180/math.pi)
    print('length', radius)
    print(180/n)
    for i in range(n):
        turtle.forward(length)
        turtle.left(rotating_angle)
        turtle.fd(radius)
        turtle.bk(radius)
        turtle.right(inside_angle)


"the time module provides a function, also named time, that returns the current grenwich mean time in 'the epoch'," \
"which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970" \
"write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the" \
"number of days since the epoch"

import time

year = math.floor(1970 + (time.time() / 31556926)) #epoch begins from the year 1970
remainder_after_year = time.time() % 31556926 #seconds past from the beginning of the current year


month = math.floor(remainder_after_year / 2629743)
remainder_after_month = remainder_after_year % 2629743 #seconds past from the beginning of the current month

day = math.floor(remainder_after_month / 86400)
remainder_after_days = remainder_after_month % 86400 #seconds past from the beginning of the current day

hour = math.floor(remainder_after_days / 3600)
remainder_after_hours = remainder_after_days % 3600 #seconds past from the beginning of the current hour

minute = math.floor(remainder_after_hours / 60)
second = int(remainder_after_hours % 60) #seconds past from the beginning of the current minute

print(year,month,day,hour,minute)

print(time.time())
print(50*31556926)
print(time.time() % 31556926)

print(time.time()-(50*31556926))