#from selenium.webdriver.firefox.webdriver import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_page(self):
        wd = self.wd
        wd.get("http://lab/addressbook/")

    def create_group(self, group):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()

    def create_contact(self, contact):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").send_keys(contact.homephone)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobilephone)
        wd.find_element(By.NAME, "work").send_keys(contact.workphone)
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(str(contact.bdate.day))
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bdate.month)
        wd.find_element(By.NAME, "byear").send_keys(str(contact.bdate.year))
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(str(contact.adate.day))
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.adate.month)
        wd.find_element(By.NAME, "ayear").send_keys(str(contact.adate.year))
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def destroy(self):
        self.wd.quit()