import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.4.731 Yowser/2.5 Safari/537.36"}
#Указываем данные браузера (чтобы не забанили)

url = f"https://garantex.io/trading/usdtrub"

def price():
    response = requests.get(url, headers=headers) #получаем тест страницы
    soup = BeautifulSoup(response.text, "lxml") #html.parser/lxml / преобразуем тестк страницы в читаемый вид
    #table = soup.find_all("price")
    table = soup.find_all("div", class_="trade_history_panel")
    #data = table.find_all("th", class_="price text-left col-xs-6 text-up")
    print(table)
price()
    
