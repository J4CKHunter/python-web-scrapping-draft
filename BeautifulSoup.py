from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#deneme linkleri :
#https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup
#https://www.bbc.com/news/health-56411561
#https://www.bbc.com
#https://nayn.co/mansur-yavas-twitch-kanali-acti-selam-chat/

#user agent farklı örnek request
#req = Request('https://nayn.co/mansur-yavas-twitch-kanali-acti-selam-chat/', headers={'User-Agent': 'XYZ/3.0'})

req = Request('https://www.bbc.com/news/health-56411561', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, "lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)


html_page = urlopen(req)

#'#footer-navigation', '#main-heading' /news/world-africa-56411157', '/news/world-asia-56408613', '/news/world-56408472', '/news/technology-56402378'
# gibi url olmayan şeyleri içermemesi için links arrayini bu şekilde tanımlıyoruz.

links = [item['href'] if item.get('href') is not None else item['src'] for item in soup.select('[href^="http"], [src^="http"]') ]

print(links)
print(len(links))