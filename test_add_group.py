# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_test_add_group(self):
        wd = self.wd
        self.open_page(wd)
        self.login(wd)
        self.create_group(wd)
        self.logout(wd)

    def open_page(self, wd):
        wd.get("http://lab/addressbook/")

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").send_keys("GRNAME")
        wd.find_element(By.NAME, "group_header").send_keys("GRHEADER")
        wd.find_element(By.NAME, "group_footer").send_keys("HRFOOTER")
        wd.find_element(By.NAME, "submit").click()

    def login(self, wd):
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try: 
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: 
            return False
        return True
    
    def is_alert_present(self):
        try: 
            self.wd.switch_to_alert()
        except NoAlertPresentException as e: 
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
