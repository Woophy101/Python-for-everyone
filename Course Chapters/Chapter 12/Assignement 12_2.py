# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url= input('Enter URL:')
url='http://py4e-data.dr-chuck.net/comments_1550959.html'
html= urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

# Retrieve all of the anchor tags
value=0
tags = soup.findAll('span',{'class':'comments'})
for tag in tags:
    #print(tag.contents[0])
    value=value+int(tag.contents[0])

print(value)
