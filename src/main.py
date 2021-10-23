import os
import time
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs

cls = lambda: os.system('cls')

def wait(timeX):
    time.sleep(timeX)

def main():
    my_url = "https://www.newegg.com/p/pl?d=graphic+card"
    print(my_url)
    uClient = ureq(my_url)

    page_html = uClient.read()

    uClient.close()

    page_soup = bs(page_html, "html.parser")

    cantainers = page_soup.find_all("div", {"class":"item-container"})

    print(len(cantainers))
    print()

    for container in cantainers:
        try:
            brand = container.a.div.div.a.img["title"]
            print(brand)
        
        except:
            print("ERROR")

    


    # print(cantainers[0].div.div.div.a.img["title"])
    # print(cantainers[0].div.a.img["title"])
    # print(cantainers[0].div.div)

    #for cantainer in cantainers:
    #    brand = 



main()