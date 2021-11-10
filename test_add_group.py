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


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://lab/addressbook/")
        # wd.find_element("user").click()
        # wd.find_element("user").clear()
        wd.find_element("user").send_keys("admin")
        # wd.find_element("pass").clear()
        wd.find_element("pass").send_keys("secret")
        wd.find_element("//input[@value='Login']").click()
        wd.find_element("groups").click()
        wd.find_element("new").click()
        wd.find_element("group_name").click()
        # wd.find_element("group_name").clear()
        wd.find_element("group_name").send_keys("grname")
        # wd.find_element("group_header").click()
        wd.find_element("group_name").click()
        wd.find_element("group_name").clear()
        wd.find_element("group_name").send_keys("GRNAME")
        wd.find_element("group_header").clear()
        wd.find_element("group_header").send_keys("GRHEADER")
        wd.find_element("group_footer").clear()
        wd.find_element("group_footer").send_keys("HRFOOTER")
        wd.find_element("submit").click()
        wd.find_element("Logout").click()
    
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
