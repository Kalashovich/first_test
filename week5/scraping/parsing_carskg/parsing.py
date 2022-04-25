import datetime
import requests
from bs4 import BeautifulSoup as bs4
#-----------------------------------------------------------------------------


# BASE_URL = 'http://www.example.com/'

# def g_html(url):
#   acces = requests.get(url)
#   return acces.text


# def g_data(acces):
#   soup = bs4(acces,'lxml')
#   catalog = soup.find_all('div')
#   for i in catalog:
#     h1 = i.find('h1').text
#     print(h1)
#     text = i.find('p').text
#     print(text)
#     url = i.find('a').get('href')
#     print(url)

# g_data(g_html(BASE_URL))

#-----------------------------------------------------------------------------

# BASE_URL = f'https://cars.kg/offers/{i}'

def get_html(url: str) -> str:
    '''
    Получает html код определенной страницы
    '''
    response = requests.get(url)
    return response.text

def get_data(html: str) -> None:
    '''
    Функция парсер, получает все данные
    '''
    soup = bs4(html,'lxml')
    # print(soup)
    catalog = soup.find('div', class_='catalog-list')
    # print(catalog)
    cars = catalog.find_all('a', class_='catalog-list-item')
    # car1 = cars[0].find('span', class_='catalog-item-caption')
    # print(car1.text.strip())
    # print(cars[1])
    for car in cars:
        title = car.find('span', class_='catalog-item-caption').text.strip()

        mileage = car.find('span', class_='catalog-item-mileage').text

        if not mileage:
            mileage = 'Без пробега'

        price = car.find('span', class_='catalog-item-price').text.strip()

        try:
            img = car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img = 'Картины нет'
        
        data = {
            'title': title,
            'meleage': mileage,
            'price': price,
            'img': img
        }
        write_to_csv(data)

        # print(f'Название {title}, Км: {mileage}, Цена: {price}, Фотка: {img}')
        # price = car.find('span', class_='')
# get_data(get_html(BASE_URL))
def write_to_csv(data: dict) -> None:
    '''
    Функция для записи данных в csv файл
    '''
    import csv
    with open('cars.csv', 'a') as file:
        fieldnames = ['Марка', 'Пробег', 'Цена', 'Фото']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            'Марка': data.get('title'),
            'Пробег': data.get('mileage'),
            'Цена': data.get('price'),
            'Фото': data.get('img')
        })
 
k = 20
i = 1

start = datetime.datetime.now()

while True:
    BASE_URL = f'https://cars.kg/offers/{i}'
    html = get_html(BASE_URL)

    catalog = bs4(html, 'lxml').find('div', class_='catalog-list')

    if i > 5:
        break
    if not catalog:
        break

    get_data(html)
    i += 1
    k += 20
    print(f'Страница: {i}, Машина: {k}')

end = datetime.datetime.now()
print(end - start)