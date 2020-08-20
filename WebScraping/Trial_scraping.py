import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

import urllib

query="'xss'"
query = urllib.parse.quote_plus(query) # Format into URL encoding
number_result = 20

ua = UserAgent()

google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "html.parser")

result_div = soup.find_all('div', attrs = {'class': 'g'})

links = []
titles = []
descriptions = []
for r in result_div:
        link = r.find('a', href = True)
        title = r.find('h3', attrs={'class': 'r'}).get_text()
        description = r.find('span', attrs={'class': 'st'}).get_text()
        
        if link != '' and title != '' and description != '':
            
            links.append(link['href'])
            titles.append(title)
            descriptions.append(description)
        print(links)
        print(type(links))        
        continue

for i in links:
            if 'owasp' in i:
               print(i)
               print("###############")
            elif 'wiki' in i:
               print(i)
