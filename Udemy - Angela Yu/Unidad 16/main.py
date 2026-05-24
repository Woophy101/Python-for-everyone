import turtle
import keyboard #Aún no se instala en linux

#Movimiento de tortuguita en tiempo real

#Settup de tortuguita
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("green","brown")

#Screen
my_screen=turtle.Screen()

#while True:
#    if keyboard.is_pressed("up"):
#        timmy.forward(25)
#    if keyboard.is_pressed("right"):
#        timmy.right(45)
#    if keyboard.is_pressed("left"):
#        timmy.left(45)
#
#Queda pendient el loop de control porque no funciona keyboard.
#Buscar alguna opcion similar para controlar con el teclado



my_screen.exitonclick()