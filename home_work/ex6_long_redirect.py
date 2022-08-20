import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

response_list = response.history

urls_list = []
i = 0
while i < len(response_list):
    urls_list.append(response_list[i].url)
    i += 1

for x in urls_list:
    print(x)
