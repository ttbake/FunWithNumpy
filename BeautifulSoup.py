from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

print(soup.prettify())
print(soup.title)

divs = soup.find_all('div', {'class': 'featured'})
for div in divs:
    print(div)

featured_header = soup.find('div', {'class': 'featured'}).h2
print(featured_header.get_text())

for button in soup.find(attrs={'class': 'button button--primary'}):
    print(button)

for link in soup.find_all('a'):
    print(link.get('href'))
