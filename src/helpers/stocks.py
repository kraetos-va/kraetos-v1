from bs4 import BeautifulSoup
from helpers.google import googleSearch
import requests

# Check Price of stock
def checkStockPrice():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        }
        for url in googleSearch("Tesla stock price yahoo finance"):
            print(url)
            page = requests.get(url, headers = headers)
            soup = BeautifulSoup(page.content, "html.parser")
            price = soup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()
            title = soup.find(class_='D(ib) Fz(18px)').get_text()
            currency = soup.find(class_='C($tertiaryColor) Fz(12px)').get_text()
            currency = currency[-3:]
            print("{} - {} - {}".format(currency, title, price))
    except AttributeError as e:
        print("Attribute Error: {}".format(e))