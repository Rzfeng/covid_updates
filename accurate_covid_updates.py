import requests
import re
from bs4 import BeautifulSoup

url = "https://www.dph.illinois.gov/covid19"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
html = response.content
doc = BeautifulSoup(html, "html.parser")
print(doc)
