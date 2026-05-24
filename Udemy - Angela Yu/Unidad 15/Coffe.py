print("\033[H\033[J", end="") #clrscr
MENU = {
    "espresso":{
        "ing":{
            "water": 50,
            "milk": 0,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ing":{
            "water": 200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ing":{
            "water": 250,
            "milk": 100,
            "coffee":24,
        },
        "cost":3.0,
    }        
}

#------------------------------------FUNCTIONS-----------------------------------
def check_ingridients(item):
    """
    Funcion que compara los ingredientes necesarios para preparar un café y los disponibles en la máquina. 
    Si alguno falta imprime un mensaje y detiene la preparación.
    """
    global water
    global milk
    global coffee
    global MENU
    status=True

    if water < MENU[item]["ing"]["water"]:
        print("❌No hay suficiente agua❌")
        status=False
    if milk < MENU[item]["ing"]["milk"]:
        print("❌No hay suficiente leche❌")
        status=False
    if coffee < MENU[item]["ing"]["coffee"]:
        print("❌No hay suficiente café❌")
        status=False
    return status

def check_payment(item):
    """
    Checkea si el pago en monedas es igual o mayor que el coste del producto.
    Si falta dinero anula la compra. NO CALCULA EL VUELTO    
    """
    global money
    status=True
    price=float(MENU[item]["cost"])

    penny=int(input("Cuántos pennys?: "))
    nickel=int(input("Cuántos nickels?: "))
    dime=int(input("Cuántos dimes?: "))
    quarter=int(input("Cuántos quarters?: "))

    payment=penny*0.01+nickel*0.05+dime*0.1+quarter*0.25

    if payment<price:
        print("Ingresaste $",payment,"el valor es de",price)
        print("❌No hay suficiente dinero❌")
        status=False

    return status


#-------------------------------------------------------------------------------

#ingredientes iniciales de la máquina
water=500
milk=300
coffee=100
money=5


print(f""" 
------------------------------------------------------------------------------
|   OPCIONES DE MENU:                                                        |   
|                                                                            |   
|    Capuccino      ${MENU['cappuccino']["cost"]}                                                     |   
|    Latte          ${MENU['latte']["cost"]}                                                     |
|    Esspreso       ${MENU['espresso']["cost"]}                                                     |
|                                                                            |       
|   MANTENIMIENTO:                                                           |           
|                                                                            |   
|    Reporte       Entrega información del inventario de la máquina          |
|    Recarga       Recarga leche, agua o caffe en una cantidad determinada   |
|    Off           Apaga la maquina                                          |
|                                                                            |   
------------------------------------------------------------------------------  
""")
{type({MENU["latte"]["cost"]})}
#Funcionamiento
while True:
    command=input("Que necesitas?: ")

#Comandos:

    #Apagado "OFF"
    if command == "off":
        break

    #Reporte
    if command =="reporte":
        print(f"""
Inventario:
    Leche:  {milk} ml
    Agua:   {water} ml
    Café    {coffee} g
    -------------------
    Dinero:  ${money}\n""")
        
    #recarga
    if command == "recarga":
        refill=input("Qué quieres recargar?: ")
        ammount=int(input("Qué cantidad?: "))

        if refill == "leche":
            milk+= ammount
            print(f"\nSe ha recargado", ammount,"de leche✅.\nCantidad total:",milk,"ml\n")

        if refill == "agua":
            water += ammount
            print(f"\nSe ha recargado", ammount,"de agua✅.\nCantidad total:",water,"ml\n")

        if refill == "cafe":
            coffee+= ammount
            print(f"\nSe ha recargado", ammount,"de café✅.\nCantidad total:",coffee,"g\n")
    
    #preparar café
    if command == "latte" or command == "cappuccino" or command == "esspreso":

        go_ingridients=check_ingridients(command)

        if go_ingridients == True:
            print(f"El valor es de ${MENU[command]["cost"]}")
            payment=check_payment(command)
            
            if payment == True:
                print(command,"listo✅!!\n")
                milk -=MENU[command]["ing"]["milk"]
                water -=MENU[command]["ing"]["water"]
                coffee -=MENU[command]["ing"]["coffee"]
                money +=MENU[command]["cost"]


#Término WHILE

print("\033[H\033[J", end="") #clrscr
print(f"""      
Maquina apagada

Inventario:
    Leche:  {milk} ml
    Agua:   {water} ml
    Café    {coffee} g
    -------------------
    Dinero:  ${money} 
""")
