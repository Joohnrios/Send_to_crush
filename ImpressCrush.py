from turtle import *
from time import sleep
import turtle


color('red')
begin_fill()


turtle.write('Your crush!', move=False, font=(
    'Comic Sans', 18, 'bold'), align='center')

tela = turtle.Screen()
tela.bgpic("backgroundRainWithFlowers.gif")

turtle.sety(-90)

pensize(8)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)

sleep(5)
end_fill
