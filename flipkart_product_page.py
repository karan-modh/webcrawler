import re
import requests
from bs4 import BeautifulSoup

def web(page, webUrl):
    flipkart_link = "https://www.flipkart.com"
    if page:
        url = webUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        product = s.findAll('a', {'class': '_1fQZEK'})[0]
        scrap = {}
        product_link = flipkart_link + product.attrs['href']
        title = product.find('div', {'class': '_4rR01T'}).contents[0]
        details = [data.contents[0] for data in product.findAll('li', {'class': 'rgWa7D'})]
        scrap[title] = {'link': product_link, 'name': title, 'details': details}
        product_page_code = requests.get(product_link)
        product_page_html_parsed = BeautifulSoup(product_page_code.text, "html.parser")
        product_title = product_page_html_parsed.find('span', {'class': "B_NuCI"}).contents[0]
        product_price = product_page_html_parsed.find('div', {'class': "_30jeq3 _16Jk6d"}).contents[0]
        highlights = product_page_html_parsed.findAll('li', {'class': "_21Ahn-"})
        highlights = [highlight.contents[0] for highlight in highlights]
        product_details = {"title": title, "price": product_price, "highlights": highlights}
        print(product_details)
        print("f")

flipkart_search_link = "https://www.flipkart.com/search?q="
suffix = "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
key = input("\nEnter your search word:\n")
flipkart_search_link += key + suffix
web(1, flipkart_search_link)


# Working for flipkart
# Amazon getting 503
