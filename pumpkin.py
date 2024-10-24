import requests 
from bs4 import BeautifulSoup

url1 = 'https://google.com'
response = requests.get(url1)
soup = BeautifulSoup(response.text, 'html.parser')

#Extract title of the page
page_title = soup.title .string
print(f"Page Title: {page_title}")

#Extract specific data (e.g, all links on the page)
all_links = soup.find_all('a')
for link in all_links:
    print(link.get('href'))