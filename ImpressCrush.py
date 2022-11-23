from turtle import *
from time import sleep
import turtle


color('red')
begin_fill()


turtle.write('Your crush!', move=False, font=(
    'Comic Sans', 18, 'bold'), align='center')


turtle.sety(-90)

pensize(8)
sleep(1)
left(50)
sleep(1)
forward(133)
sleep(1)
circle(50, 200)

sleep(1)
right(140)
sleep(1)
circle(50, 200)
sleep(1)
forward(133)

sleep(5)
end_fill
