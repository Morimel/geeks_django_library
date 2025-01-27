import requests
from bs4 import BeautifulSoup as BS

URL = 'https://knigochet.com/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
}


#1 

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


#2 
def get_data(html):
    bs = BS(html, features="html.parser")
    sect_content = bs.find('div', class_='sect-content')  # Найти основной контейнер
    mybook_list = []
    if sect_content:  # Проверить, найден ли контейнер
        items = sect_content.find_all('a', class_='poster-item')  # Найти все книги
        for item in items:
            title_tag = item.find('div', class_='poster-item__title')  # Заголовок внутри каждой книги
            title = title_tag.get_text(strip=True) if title_tag else "No title found"
            mybook_list.append({
                'title': title,
            })
    return mybook_list



#3

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        mybook_list2 = []
        for page in range(1, 2):
            response = get_html(f"https://knigochet.com/cat_5", params={'page': page})
            mybook_list2.extend(get_data(response.text))
        return mybook_list2
    else:
        raise Exception('Error in parsing')
    
    
# print(parsing())