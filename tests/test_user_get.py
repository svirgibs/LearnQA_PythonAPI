import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("User get cases")
class TestUserGet(BaseCase):
    @allure.description("This test successfully get not auth user username field")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("This test successfully get auth user fields")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("This test successfully get not auth user as same user username field")
    def test_get_user_details_not_auth_as_same_user(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        response2 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        incorrect_user_id = 2

        response3 = MyRequests.get(f"/user/{incorrect_user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_field = "username"
        not_expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_key(response3, expected_field)
        Assertions.assert_json_has_no_keys(response3, not_expected_fields)
