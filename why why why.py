from bs4 import BeautifulSoup
import requests
print("wait...")
while(0.1):
    response = requests.get("https://www.gismeteo.ua/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("", {"href": f"/ua/weather-zbarazh-11874/now/"})
        res = soup_list[0].find("span")
        print(res.text)