from bs4 import BeautifulSoup
import requests
print("wait...")
class searcher():
    # Function to add two numbers
    def add(num1, num2):
        return num1 + num2

    # Function to subtract two numbers
    def subtract(num1, num2):
        return num1 - num2

    # Function to multiply two numbers
    def multiply(num1, num2):
        return num1 * num2

    # Function to divide two numbers
    def divide(num1, num2):
          return num1 / num2
    def raisetodegree(num1, num2):
          return num1 ** num2
    print("Please select operation -\n" \
              "1. Add\n" \
              "2. Subtract\n" \
              "3. Multiply\n" \
              "4. Divide\n"
              "5. Raise to degree\n")

        # Take input from the user
    select = int(input("Select operations from 1, 2, 3, 4, 5 :"))

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
            print(number_1, "+", number_2, "=",
                 add(number_1, number_2))
    elif select == 2:
            print(number_1, "-", number_2, "=",
                 subtract(number_1, number_2))

    elif select == 3:
            print(number_1, "*", number_2, "=",
                 multiply(number_1, number_2))

    elif select == 4:
            print(number_1, "/", number_2, "=",
                 divide(number_1, number_2))
    elif select == 5:
            print(number_1, "**", number_2, "=",
                 raisetodegree(number_1,number_2))
    else:
            print("Invalid input")
    print("Connected! Follow the steps below")
    response = requests.get("https://coinmarketcap.com/")
    currency = input("Type a name of currency without any spelling mistakes( all lowercase ): ")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("a", {"href": f"/currencies/{currency}/markets/"})
        res = soup_list[0].find("span")
        print(res.text)
        coin_value = float(res.text.strip("$").replace(",",""))
        # filters out $ and , from the number received and turns it into a float type
        print("Input the number you received from operations")
        results = float(input())
        print(f"you own {divide(results, coin_value)} of {currency}! Congratulations!")
searcher()

