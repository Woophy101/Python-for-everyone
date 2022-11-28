#Exercise 2: Change your socket program so that it counts the number
#of characters it has received and stops displaying any text after it has
#shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
#of the number of characters at the end of the document.

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

while True:
    file=input('File?:')
    cmd='GET http://'+url+'/'+file+' HTTP/1.0\r\n\r\n'
    UT8=cmd.encode()
    if url=='done':
        break
    try:
        if (mysock.send(UT8)):
            print('Valid File!')
            break
    except:
        print('Invalid File')
        continue

txt=b''

while True:
    data = mysock.recv(512) 
    if (len(data)<1):
        break
    txt=txt+data   
mysock.close()

pos=txt.find(b'\r\n\r\n')   #Encontrar donde termina el Metadata
print('Headder end at:',pos)
ctxt=(txt[pos+4:].decode())   #Eliminar Metadata, el +4 elimina un par de lineas blancas /r/n/r/n(no se si afectan en la cuenta). "clean text"


print(ctxt[:3000]) #mostrar los 3000 primeros caracteres del archivo. En una paginaonline aparece que son mas de 3000 caracteres, hay que chequear bien a que se reiere



