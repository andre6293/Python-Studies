from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://genius.com/albums/Nick-cave-and-the-bad-seeds/Henry-s-dream'

req = Request(my_url, headers = { 'User-Agent' : 'Mozilla/5.0' })
page_html = urlopen(req).read()

page_soup = soup(page_html, "html.parser")

print(page_soup)