import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

response_list_history = response.history

urls_list = []
i = 0
while i < len(response_list_history):
    urls_list.append(response_list_history[i].url)
    i += 1

urls_list.append(response.url)

for x in urls_list:
    if x is urls_list[-1]:
        print(f"Last url: {x}")
        break
    print(x)
