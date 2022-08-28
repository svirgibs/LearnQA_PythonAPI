import requests


class TestRequestHeader:
    def test_request_on_method_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers_dict = dict(response.headers)
        assert headers_dict['x-secret-homework-header'] == "Some secret value"
