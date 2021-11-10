# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="GR.NAME", header="GR.HEADER", footer="GR.FOOTER"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def open_page(self, wd):
        wd.get("http://lab/addressbook/")

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, wd, group):
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
