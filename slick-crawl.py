from bs4 import BeautifulSoup
import requests
import sys

#get slickdeals.net
url = 'https://slickdeals.net'
content = requests.get(url).text
soup = BeautifulSoup(content, 'html.parser')

frontpage = soup.find_all('div', class_='priceLine')

print(frontpage[0])
#print(frontpage[0].find_next_sibling('div', class_='listPrice'))

#for item in frontepage:
#    print("Title: {}".format())