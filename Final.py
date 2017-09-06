import requests
from bs4 import BeautifulSoup

file = open("testfile.txt","w")

res = requests.get('https://clarity-project.info/tenders/?entiy=38163425&offset=100').text
soup = BeautifulSoup(res,"lxml")
for item in soup.find_all(class_="table-row"):
    try:
        file.write(item.get('data-id')+'\n')
    except:
        continue
    print(item.get('data-id'))
file.close()
