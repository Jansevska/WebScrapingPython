from bs4 import BeautifulSoup
import requests

# url root
root = 'https://subslikescript.com'

# To get the HTML content of a web page, we use the requests library and the get() method
url = f"{root}/movies"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# To find a single element, we use the find() method -> returnns one element
box = soup.find('article', class_='main-article')

# Find ALL ''a' tags -> Using boolean to find all href elements -> find_all() returns a LIST
links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)

for link in links:
    url = f"{root}/{link}"
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)