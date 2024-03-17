from bs4 import BeautifulSoup
import requests

# To get the HTML content of a web page, we use the requests library and the get() method.
url = "https://subslikescript.com/movie/Titanic-120338"
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'lxml')

# We can use the find() method to find the first occurrence of a tag with a given class or id.
box = soup.find('article', class_='main-article')

# title = box.find('h1').get_text()  OR

# Locate title by finding the first occurrence of the h1 tag in the article tag.
# We can use the get_text() method to get the text content of a tag.
title = soup.find('article', class_='main-article').h1.get_text()
print(title)

# Locate the transcript by finding the first occurrence of the div tag with the class full-script.
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# I didn't have encoding='utf-8' and it gave a UnicodeEncodeError
with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
    

# Writing to a file with ANSI encoding or UnicodeEncodeError occurs

# Writing to a file with UTF-8 encoding
with open('filename.txt', 'w', encoding='utf-8') as f:
    f.write('Some text that includes non-ASCII characters like é, ö, or ç')

# Reading from a file with UTF-8 encoding
with open('filename.txt', 'r', encoding='utf-8') as f:
    content = f.read()