import requests
import json
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1 - создание задачи
response_start = requests.get(url)
answer = json.loads(response_start.text)
token = answer['token']

# 2 - запрос до того, как задача готова
response_check_before = requests.get(url, params={"token": token})
assert response_check_before.text == '{"status":"Job is NOT ready"}'

# 3 - ждем нужное количество секунд
time.sleep(answer['seconds'])

# 4 - запрос с токеном, когда задача готова
response_check = requests.get(url, params={"token": token})
assert response_check.text == '{"result":"42","status":"Job is ready"}'

