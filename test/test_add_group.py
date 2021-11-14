# -*- coding: utf-8 -*-
#from selenium import webdriver
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

def test_add_group(app):
    app.open_page()
    app.login(username="admin", password="secret")
    app.create_group(Group(name="GR.NAME", header="GR.HEADER", footer="GR.FOOTER"))
    app.logout()

def test_add_empty_group(app):
    app.open_page()
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

