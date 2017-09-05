#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://clarity-project.info/tenders/?entity=38163425&offset=100'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36\
(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

request = Request(url, headers={'User-Agent': agent})

html = urlopen(request).read().decode()

soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll(lambda tag: tag.get('data-id', None) is not None)
for tag in tags:
    print(tag['data-id'])
    
    

path = "/Users/tinasosiak/Documents/number.txt"
days_file = open(path,'r')
days = days_file.read()


new_path ="/Users/tinasosiak/Documents/number.txt"
new_days = open(new_path,'w')

title = tag['data-id']
    
new_days.write(title)
print(title)

new_days.write(days)
print(days)

days_file.close()
new_days.close()
