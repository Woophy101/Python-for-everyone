#Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the
#count of the paragraphs as the output of your program. Do not display
#the paragraph text, only count them. Test your program on several
#small web pages as well as some larger web pages.
#NOTA: lo hice sin usar URLLIBS porque me da mucho error

import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    url=input('Url?:')
    try:
        mysock.connect((url,80))
        print('Connected to URL!')
        break
    except:
        print('Invalid URL')
        continue

while True:
    try:
        file=input('File?:')
        cmd='GET http://'+url+'/'+file+' HTTP/1.0\r\n\r\n'
        UT8=cmd.encode()
        if (mysock.send(UT8)):
            print('File Found!')
            break
    except:
        print('File not found')
        continue


cmd='GET http://'+url+'/'+file+' HTTP/1.0\r\n\r\n'
UT8=cmd.encode()
mysock.send(UT8)

btxt=b''
while True:
    data = mysock.recv(512)
    btxt=btxt+data
    if (len(data)<1):
        break
mysock.close()

print(data.decode())
pos=btxt.find(b'\r\n\r\n')
print('Headder starts at:',pos)

fh=btxt.decode()
txt=fh[pos+4:]

count=0
for lines in txt:
    if lines==('\n'):
        count=count+1

print(count)
