#Exercise 1: Change the socket program socket1.py to prompt the user
#for the URL so it can read any web page. You can use split('/') to
#break the URL into its component parts so you can extract the host
#name for the socket connect call. Add error checking using try and
#except to handle the condition where the user enters an improperly
#formatted or non-existent URL.

import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    url=input('URL?:')
    if url=='done':
        break
    try:
        mysock.connect((url,80))
        print('Valid URL')
        break
    except:
        print('Invalid URL')
        continue
file=input('file?')
cmd='GET http://'+url+file' HTTP/1.0\r\n\r\n' .encode()'
print(cmd)
mysock.send(cmd)


while True:
    data = mysock.recv(512) #tamaño del paquete de datos que quiero enviar o recibir
    if (len(data)<1):
        break
    print(data.decode())
mysock.close() #siempre serrar el socket, gasta recursos al usuario y al servidor
