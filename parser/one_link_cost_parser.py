import requests
from bs4 import BeautifulSoup


def get_html_by_requests(url, useragent=None, params=''):
        try:
            r = requests.get(url, headers=useragent, params=params)
        except:
            r = False
            print(".......... get_html_by_requests -> False")
            return(get_contents_by_bs(r))
        else:
            print(r)
            return(get_contents_by_bs(r))


def get_contents_by_bs(html):  # на входе список из объектов response
    if html != False:

        soup = BeautifulSoup(html.text, 'html.parser')
        # берем текст у каждого объекта response из списка
        # ищем название товара
        try:
            # ищем стоимость товара
            bs4_price = soup.find("div", {"class": "price-label--primary"})
            bs4_price_rub = bs4_price.find(("span", {"class": "price-label__integer"}))
            price_rub = bs4_price_rub.text.strip()

            bs4_price_cop = bs4_price.find(("small", {"class": "price-label__fraction"}))
            price_cop = bs4_price_cop.text.strip()
        except:
            cost = "not found"
            return(cost)
        else:
            cost = (f"{price_rub}.{price_cop}").replace(" ", "")
            return(cost)
    else:
        print(".......... get_contents_by_bs -> not found")
        cost = "not found"
        return(cost)
