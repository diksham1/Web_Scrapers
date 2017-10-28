#The script scrapes data as present on https://coinranking.com

from urllib2 import urlopen as open
from bs4 import BeautifulSoup as soup

url = 'https://coinranking.com'

client = open(url)
page = client.read()

page = soup(page,'html.parser')

container = page.find_all('div')
