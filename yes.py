import requests
response = requests.get("https://www.bloomberg.com/quote/USDUAH:CUR")
response_text = response.text
response_parse = response_text.split("<span>")
def result():
    for parse_elem_2 in parse_elem_1.split("</span>"):
        if parase_elem_2.startswith("3") and parse_elem_2[1].isdigit():
            print(parse_elem_2)
for parse_elem_1 in response_parse:
    ### its supposed to parse the page for </span>'s a
    if parse_elem_1.startswith("1"):
        result()
    elif parse_elem_1.startswith("2"):
        result()
    elif parse_elem_1.startswith("3"):
        result()
    elif parse_elem_1.startswith("4"):
        result()
    elif parse_elem_1.startswith("5"):
        result()
    elif parse_elem_1.startswith("6"):
        result()
    elif parse_elem_1.startswith("7"):
        result()
    elif parse_elem_1.startswith("8"):
        result()
    elif parse_elem_1.startswith("9"):
        result()
"""sample code ahead ( this code was purely based on it )\



import requests
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                print(parse_elem_2)"""