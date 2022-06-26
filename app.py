from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

url = ''

# page = requests.get(url)
# soup = BeautifulSoup(page.content,'html.parser')
# with open('app.html','wb+') as file:
#     file.write(page.content)
# mydivs = soup.find_all('div',class_='js-item_body')
# print(mydivs)

session = HTMLSession()
r=session.get(url)

res = r.html.find('.searchs_property_body js-searchs_property_body')
print(res)