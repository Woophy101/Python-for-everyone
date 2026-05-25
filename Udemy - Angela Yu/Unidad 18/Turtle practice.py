from turtle import Turtle, Screen



ttt=Turtle()
my_screen = Screen()

###Draw a square
"""
for steps in range(100):
    size=150                     #Cantidad de pasos de la tortgatortuga
    for c in ("blue","red","green","brown"):       #Rotacion de colores por segmento
        ttt.color(c)                                #Define el color del segmento
        ttt.forward(size)                            #Mueve la tortuga
        ttt.right(90)
"""


#Draw a polygon
"""
for steps in range(100):
    size=10                       #Cantidad de pasos de la tortgatortuga
    for c in ("blue","red","green","brown"):       #Rotacion de colores por segmento
        ttt.color(c)                                #Define el color del segmento
        ttt.forward(size)                            #Mueve la tortuga
        ttt.right(44)
        size +=size
"""

#Make lines untill origin is reached
"""
ttt.begin_fill()
while True:
    ttt.forward(200)
    ttt.left(170)
    if abs(ttt.pos()) < 1:
        break

ttt.end_fill()
"""

#Dashed Line
"""
for steps in range(5):
    ttt.pendown()
    ttt.forward(25)
    ttt.penup()
    ttt.forward(25)
"""


#Draw consecutive polygons 
print("\033[H\033[J", end="") 

edge=100
counter = 3           #lados del poligono inicial
max_count=10        #lados del ultimo poligono dibujado
angle=360/counter   #Se usa calculando el angulo exterior de un polígono

while True:
    
    if counter == max_count:    #Dejar de dibujar
        break
    for colors in ("green","red","blue"):
    
            #Si el ciclo no se rompe, dibujar el poligono
        ttt.color(colors)
        ttt.forward(edge)
        ttt.right(angle)

        if abs(ttt.pos()) < 1:  #checkear si TTT llegó al origen para dibujar un nuevo poligono
            counter +=1
            angle = 360/counter
        

my_screen.exitonclick()


