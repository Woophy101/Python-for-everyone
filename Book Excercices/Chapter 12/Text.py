import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #similar al file habdler pero con un socket
mysock.connect(('data.pr4e.org',80)) #Genera la conección con el servidor
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode() #se define un comando. Encode permite cambiarr de Unicode a UTF-8 (tiene que ver con la comunicacion del servidor, es cambiar de "idioma")
mysock.send(cmd) #se envia el comando al servidor

while True:
    data = mysock.recv(512) #tamaño del paquete de datos que quiero enviar o recibir
    if (len(data)<1):
        break
    print(data.decode())
mysock.close() #siempre serrar el socket, gasta recursos al usuario y al servidor
