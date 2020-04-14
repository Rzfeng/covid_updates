import requests
import re
from bs4 import BeautifulSoup

chicago_url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Illinois"
wisconsin_url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Wisconsin"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(chicago_url, headers=headers)
html = response.content
doc = BeautifulSoup(html, "html.parser")
table = doc.find('table', attrs={'class': 'wikitable sortable'})
tr = table.find_all('tr')

cook_data = []
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    for td in tds:
        if "Cook" in str(td):
            cook_data = tds

county_name = cook_data[0].text.strip()
count = cook_data[1].text.strip()
deaths = cook_data[2].text.strip()
recovered = cook_data[3].text.strip()
clean_cook_data = []
clean_cook_data.append(county_name)
clean_cook_data.append(count)
clean_cook_data.append(deaths)
clean_cook_data.append(recovered)

print(clean_cook_data)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(wisconsin_url, headers=headers)
html = response.content
doc = BeautifulSoup(html, "html.parser")
table = doc.find('table', {'class': 'wikitable plainrowheaders sortable mw-collapsible mw-collapsed'})
dane_data = []
for tr in table.find_all('tr'):
    county1 = tr.find(text="Dane")
    county2 = tr.find(text="Milwaukee")
    county3 = tr.find(text="Waukesha")
    if county1 != None:
        dane_data = re.sub('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', '', str(tr)).split()
    # tds = tr.find_all('td')
    # print(tds)
dane_county_name = dane_data[0]
dane_positive = dane_data[1]
dane_negative = dane_data[2]
dane_deaths = dane_data[3]
#
# for i in range(len(dane_data)):
#     print(val.text.strip())
