import requests
import bs4

url= "https://izmeritel.in.ua/site_search?search_term=0011"
t= requests.get(url)
t.encoding = "UTF8"


b=bs4.BeautifulSoup(t.text, "html.parser")
atitles = b.select( "div.cs-product-gallery__info-panel a")

titles = []
for a in atitles:
    titles.append(a.getText())

print(titles)
