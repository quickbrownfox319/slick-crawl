from bs4 import BeautifulSoup
import urllib2
import sys

#get slickdeals.net
url = 'https://slickdeals.net'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')

frontpage = soup.find('div', class_='data-module-item')

print(frontpage)
#for item in result:
#    print(item.prettify())