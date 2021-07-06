import requests
from bs4 import BeautifulSoup
from itertools import cycle


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = BeautifulSoup(response.text, "html.parser")
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                             i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


proxies = get_proxies()
proxy_pool = cycle(proxies)
url = 'https://httpbin.org/ip'
for i in range(1, 10):
    proxy = next(proxy_pool)
    print("Request #%d" % i)
    print("IP: " + proxy)
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        print("Skipping. Connnection error")
