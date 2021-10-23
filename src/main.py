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

    cantainers = page_soup.find_all("div", {"class":"item-cell"})

    print(len(cantainers))
    print()

    for container in cantainers:
        try:
            #item_cell_13-145-240_1_0 > div > div.item-info > div > a.item-brand > img
            brand = container.div.div.div.a.img["title"]
            print(brand)
            #item_cell_13-145-240_1_0 > div > a > img
            print()
            item_name = container.div.a.img["title"]
            print(item_name)
            print()
            #item_cell_13-145-240_1_0 > div > div.item-action > ul > li.price-current > strong
            #item_cell_13-145-240_1_0 > div > div.item-action > ul > li.price-current > sup
            item_price = container.div.div.ul.li.strong
            item_price_2 = container.div.div.ul.li.sup
            print(item_price + item_price_2)
            print()
        
        except:
            print("No Brand Name")
            print("No Name")
            print()

    


    # print(cantainers[0].div.div.div.a.img["title"])
    # print(cantainers[0].div.a.img["title"])
    # print(cantainers[0].div.div)

    #for cantainer in cantainers:
    #    brand = 



main()