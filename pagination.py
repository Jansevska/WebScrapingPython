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

# pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
# [-2] because you want one item before the last, the last item is an arrow
last_page = pages[-2].text

links = [] # moved links=[] outside the loop
# for page in range(1, 1794+1): # range(1, 1794+1)
for page in range(1, int(last_page)+1): # range(1, 1794+1)
    response = requests.get(f"{url}?page={page}")
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    # To find a single element, we use the find() method -> returnns one element
    box = soup.find('article', class_='main-article')

    # Find ALL ''a' tags -> Using boolean to find all href elements -> find_all() returns a LIST
    
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            print(link)
            url = f"{root}/{link}"
            response = requests.get(url)
            content = response.text
            soup = BeautifulSoup(content, 'lxml')
            
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            
            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            # if one link doesn't work, goes to the next link
            print("----- Link not working -----")
            print(link)
        