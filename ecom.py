import requests
from bs4 import BeautifulSoup

def web(page, webUrl):
    flipkart_link = "https://www.flipkart.com"
    if page:
        url = webUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        products = s.findAll('a', {'class': '_1fQZEK'})
        scrap = {}
        for product in products:
            product_link = flipkart_link + product.attrs['href']
            title = product.find('div', {'class': '_4rR01T'}).contents[0]
            details = [data.contents[0] for data in product.findAll('li', {'class': 'rgWa7D'})]
            scrap[title] = {'link': product_link, 'name': title, 'details': details}
        print(scrap)
            

flipkart_search_link = "https://www.flipkart.com/search?q="
suffix = "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
key = input("\nEnter your search word:\n")
flipkart_search_link += key + suffix
web(1, flipkart_search_link)


# Working for flipkart
# Amazon getting 503                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            