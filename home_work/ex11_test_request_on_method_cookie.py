import requests


class TestRequest:
    def test_request_on_method_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_dict = dict(response.cookies)
        assert cookie_dict['HomeWork'] == 'hw_value'
