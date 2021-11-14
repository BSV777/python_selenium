# -*- coding: utf-8 -*-
#from selenium import webdriver
#from selenium.webdriver.common.by import By
import unittest
from models import *
from application import Application

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.open_page()
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="GR.NAME", header="GR.HEADER", footer="GR.FOOTER"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.open_page()
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
