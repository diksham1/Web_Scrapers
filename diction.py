#This is a script to scrape the web and find the meaning of a word

import urllib2
from bs4 import BeautifulSoup as soup

url = 'https://en.oxforddictionaries.com/definition/' 

word = raw_input();

while(not(word == 'q')):

    newurl = url + word
    client = urllib2.urlopen(newurl)
    page = client.read()
    page = soup(page, 'html.parser')
    meaning = str(page.find('meta',{'name':'description'}))
        
    fhand = open('cr.html','w')
    fhand.write(str(page))
    
    start = meaning.find(' - ') + 2
    end = meaning.find('" name')
    meaning = meaning[start:end]

    print word + ':' + meaning

    word = raw_input()

    fhand.close()
    client.close()
