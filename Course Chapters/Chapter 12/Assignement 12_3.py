# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

scycles=input('Number of cycles:')
ncycles=int(scycles)
scount=input('Enter position:')
ncount=int(scount)
url = input('Enter URL to start:')

cycles=0
while cycles<ncycles:
    count=0
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        count=count+1    
        if count==ncount:
            print('Retriving:',tag.get('href', None))
            url = tag.get('href',None)
    cycles=cycles+1
    