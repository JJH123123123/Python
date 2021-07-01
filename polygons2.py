from sys import exit
from turtle import *
from math import sqrt, cos, radians

def tria():
    speed(6)
    seth(180)
    fd(radius*sqrt(3))
    lt(120)
    fd(radius *sqrt(3))
    lt(120)
    fd(radius * sqrt(3))
    seth(120)
  

def rect():
    speed(6)
    seth(0)
    fd(radius * sqrt(2))
    rt(90)
    fd(radius * sqrt(2))
    rt(90)
    fd(radius * sqrt(2))
    rt(90)
    fd(radius * sqrt(2))
    seth(0)

def penta():
    speed(6)
    seth(-36)
    fd(cos(radians(54))*radius*2)
    rt(72)
    fd(cos(radians(54))*radius*2)
    rt(72)
    fd(cos(radians(54))*radius*2)
    rt(72)
    fd(cos(radians(54))*radius*2)
    rt(72)
    fd(cos(radians(54))*radius*2)
    seth(180)

def hexa():
    speed(6)
    seth(-30)
    fd(radius)
    rt(60)
    fd(radius)
    rt(60)
    fd(radius)
    rt(60)
    fd(radius)
    rt(60)
    fd(radius)
    rt(60)
    fd(radius)
    seth(180)

def one():
    speed(6)
    seth(225)
    circle(radius)
    seth(0)

def outercircle():
    speed(6)
    circle(radius)
    seth(0)


screen = getscreen()
radius = float(screen.numinput("20보다 큰 값을 입력해주세요", "prompt", 0, 20))
shape('turtle')
speed(6)

screen.listen()
screen.onkeypress(reset,"r") 
screen.onkeypress(exit,"q")
screen.onkeypress(tria,"3")
screen.onkeypress(rect,'4')
screen.onkeypress(penta,'5')
screen.onkeypress(hexa,'6')
screen.onkeypress(one,'o')
screen.onkeypress(outercircle,'C')

    

screen.mainloop()
