from bs4 import BeautifulSoup
import requests
print("wait...")
while(0.1):
    print("Connected! Follow the steps below")
    response = requests.get("https://coinmarketcap.com/")
    currency = input("Type a name of currency without any spelling mistakes( all lowercase ): ")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("a", {"href": f"/currencies/{currency}/markets/"})
        res = soup_list[0].find("span")
        print(res.text)