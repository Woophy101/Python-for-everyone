offers={}

while True:
    name=input("Ingrese nombre del participante:")
    bid=int(input("Ingrese oferta:"))
    offers[name]=bid

    test=input("Agregar mas participantes? Y/N:")
    if test == "y":
        continue
    if test == "n" or test =="N":
        break

high_bid=0
high_bidder=""

for keys in offers:
    if offers[keys] > high_bid:
        high_bidder=keys
        high_bid=offers[keys]
       

print(f"Substa ganada por: {high_bidder} con un valor de {high_bid} ")

