from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

artist = (input('What artist would you like to get information about? ')).replace(' ' , '_')

my_url = 'https://pt.wikipedia.org/wiki/{}'.format(artist)

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

artist_table = page_soup.tbody.text.replace('\n\n', '\n')

print(artist_table)
f = open('scrape.txt','w')
f.write(artist_table)