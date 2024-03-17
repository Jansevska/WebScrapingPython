from bs4 import BeautifulSoup
import requests

# To get the HTML content of a web page, we use the requests library and the get() method.
url = "https://subslikescript.com/movies"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# We can use the find() method to find the first occurrence of a tag with a given class or id.
box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)