import requests
from bs4 import BeautifulSoup
url = "https://www.thewhiskyexchange.com"
r = requests.get(url)
print(r.status_code)
content = "r.texet"
soup = BeautifulSoup(content, "html.parser")
body = soup.find("body")
wrapper = body.find("div", id="wrapper")
redesign = wrapper.find('div', {'class': 'redesign'})
page_content = redesign.find('div', id="pagecontent")
pg_content = page_content.find_all('div', {'class': 'pagecontent'})[2]
cont2 = pg_content.find('div', id="content-2-wide")
main = cont2.find('div', id="main")
article = main.find('div',{'class':'article'})
ab_widget = article.find('span',{'class':'ab_widget'})
seen_coll = ab_widget.find('div',{'class':'seen-collection'})
article2 = seen_coll.find('div',{'class':'article'})
lister = article2.find('div', {'class':'lister'})
table = lister.find('table')
tbody = lister.find('tbody')
all_wine = tbody.find_all('tr')
for i in all_wine:
      title_col = i.find('td',{'class':'titleColumn'})
      rating_col = i.find('td', {'class': 'ratingColumn imdbRating'})
      text = title_col.a.text
      rating = rating_col.strong.text
      print(text, rating)
print(all_wine)
