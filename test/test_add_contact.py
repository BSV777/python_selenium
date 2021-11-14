# -*- coding: utf-8 -*-
#from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#import unittest
import pytest
from models import *
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="test", middlename="test", lastname="test",
                                    nickname="test", title="test", company="test",
                                    address="test", homephone="test", mobilephone="test",
                                    workphone="test", fax="test", email="test", email2="test",
                                    email3="test", homepage="test",
                                    bdate=ContactDate(1, "January", 2001),
                                    adate=ContactDate(2, "February", 2002),
                                    address2="test", phone2="test", notes="test"))
    app.session.logout()
