from bs4 import BeautifulSoup
import requests

listlink=[]

def aparat():
    url=requests.get(input('Type Url '))
    soup=BeautifulSoup(url.text,'lxml')

    link=soup.select('li.menu-item-link.link a')

    for i in link:
        
            
        listlink.append(i.attrs['href'].split('?w')[:1])


    print(listlink)


aparat()




