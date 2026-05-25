from turtle import Turtle, Screen
from colors import VIBRANT_COLORS as COLORS
import random

print("\033[H\033[J", end="") 

#Condiciones de la tortuga
ttt= Turtle()
my_screen = Screen()
steps=0
max_steps=100
ttt.pensize(10)
ttt.speed("fast")

#configuracion ráppida de parametros
mov_angle=90
mov_dist=50   


while True:
    movement=random.randrange(0,360,mov_angle)  #Randomiza dirección
    ttt.color(random.choice(COLORS))            #Randomiza Color
    ttt.setheading(movement)                    #Rota a la tortuga a la dirección
    ttt.forward(mov_dist)                       #mMueve en la distancia preestablecida

    if steps == max_steps:
        break
    else:
        steps +=1

my_screen.exitonclick()
    
