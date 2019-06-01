from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup as soup

from lxml.html import fromstring
from requests import get

query = input ( 'Query: ' )

raw = get("https://www.google.com/search?q=" + query).text
page = fromstring(raw)
page_soup = soup(raw,"html.parser")

print ( 'Results: ' )

for result in soup.select(".r a"):
	print(result)
  