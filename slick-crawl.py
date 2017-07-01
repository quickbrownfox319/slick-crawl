from bs4 import BeautifulSoup
import requests
import sys

#get slickdeals.net
url = 'https://slickdeals.net'
content = requests.get(url).text
soup = BeautifulSoup(content, 'html.parser')

#frontpage = soup.find_all('div', class_='priceLine')

frontpage = soup.find_all('div', class_='fpGridBox')

print(frontpage[0].attrs['fpGridBox'])


'''
for item in frontpage:
    print(item.attrs['title'])
'''