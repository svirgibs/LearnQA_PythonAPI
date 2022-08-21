from selenium import webdriver
import unittest


class GetCommonPasswords(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

    def test_get_common_passwords(self):
        self.get_common_passwords_list()

    def get_common_passwords_list(self):
        wd = self.driver
        pass_list_long = []
        for element in wd.find_elements("xpath", "//div[@id='mw-content-text']/div/table[3]/tbody/tr")[1:]:
            tds_list = element.find_elements("css selector", "td")[1:]
            for td in tds_list:
                password = td.text
                pass_list_long.append(password)
        pass_list = list(set(pass_list_long))
        return pass_list

    def tearDown(self):
        self.driver.quit()
