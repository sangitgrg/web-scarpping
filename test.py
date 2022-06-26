from bs4 import BeautifulSoup
import requests
url = ""
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)