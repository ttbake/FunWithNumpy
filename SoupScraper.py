from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

site_links = []

def internal_links(linkURL):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'
                   .format(linkURL))
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find('a', href=re.compile('(.html)$'))

def external_links(linkURL):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'
                   .format(linkURL))
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find('a', href=re.compile('(^https://)'))

if __name__ == '__main__':
    urls = internal_links('index.html')
    external_urls = external_links('index.html')
    while len(urls) > 0:
        page = urls.attrs['href']
        if page not in site_links:
            site_links.append(page)

            print(page)
            print('\n======================\n')
            urls = internal_links(page)
        else:
            break
    while len(external_urls) > 0:
        page = external_urls.attrs['href']
        if page not in site_links:
            site_links.append(page)

            print(page)
            print('\n======================\n')
            external_urls = external_links(page)
        else:
            break

