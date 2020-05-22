import urllib2
from bs4 import BeautifulSoup

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip()
print(name)

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)