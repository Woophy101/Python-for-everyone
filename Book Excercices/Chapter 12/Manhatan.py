import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


#---------------------------------------------------------------------

# Ignore SSL certificate errors    AUN NO SE PARA QUE ES ESTO



#--------------------------IMPUT DE SITIO Y ARCHIVO-------------------------------
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    site=input('Url?:')
    try:
        mysock.connect((site,80))
        print('Connected to URL!')
        break
    except:
        print('Invalid URL')
        continue

#------------------------------RECIBIR DATA DESDE URL--------------------------------

while True:
    try:
        file=input('File?:')
        cmd='GET http://'+site+'/'+file+' HTTP/1.0\r\n\r\n'
        UT8=cmd.encode()
        if (mysock.send(UT8)):
            print('File Found!')
            break
    except:
        print('File not found')
        continue

url=str(site+'/'+file)
cmd='GET http://'+site+'/'+file+' HTTP/1.0\r\n\r\n'
UT8=cmd.encode()
mysock.send(UT8)

#---------------------------INFORMACION SACADA CON SOCKET----------------------------

btxt=b''
while True:
    data = mysock.recv(512)
    btxt=btxt+data
    if (len(data)<1):
        break
mysock.close()

pos=btxt.find(b'\r\n\r\n')
#print('Headder starts at:',pos)

fh=btxt.decode()

print('----------------------METADATA------------------------')
print(fh[:pos])
print('------------------------INFO--------------------------')
print(fh[pos+4:])

#-----------------------------SACAR DATOS ESPECIFICOS CON URLLIB------------------------------


print('-----------------------URLLIB-------------------------')
html=(site+'/'+file)
print('Requesting:',html)
fhand= urllib.request.urlopen(html)
soup = BeautifulSoup(fhand, "html.parser")
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

