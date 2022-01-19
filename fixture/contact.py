from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
from time import sleep
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements(By.NAME, "add")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()
        Select(wd.find_element(By.NAME, "group")).select_by_value("")

    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if contact.bdate is not None:
            Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(str(contact.bdate.day))
            Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bdate.month)
            wd.find_element(By.NAME, "byear").send_keys(str(contact.bdate.year))
        if contact.adate is not None:
            Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(str(contact.adate.day))
            Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.adate.month)
            wd.find_element(By.NAME, "ayear").send_keys(str(contact.adate.year))
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contacts_page()
        self.contact_cache = None
        # !!!
        sleep(1)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contacts_page()
        self.contact_cache = None
        # !!!
        sleep(1)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # self.select_contact_by_index(index)
        # wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.open_contacts_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # self.select_contact_by_index(index)
        # wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.open_contacts_page()
        self.contact_cache = None


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element(By.CSS_SELECTOR, "[href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                # all_phones = cells[5].text.splitlines()
                # self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                #                                   homephone=all_phones[0], mobilephone=all_phones[1],
                #                                   workphone=all_phones[2], secondaryphone=all_phones[3]))
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text)
        homephone = "" if homephone is None else homephone.group(1)
        workphone = re.search("W: (.*)", text)
        workphone = "" if workphone is None else workphone.group(1)
        mobilephone = re.search("M: (.*)", text)
        mobilephone = "" if mobilephone is None else mobilephone.group(1)
        secondaryphone = re.search("P: (.*)", text)
        secondaryphone = "" if secondaryphone is None else secondaryphone.group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_group_by_id(self, id):
        wd = self.app.wd
        Select(wd.find_element(By.NAME, "to_group")).select_by_value(id)
        wd.find_element(By.XPATH, "//input[@value='Add to']").click()

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(contact_id)
        self.add_contact_to_group_by_id(group_id)
        self.open_contacts_page()
        self.contact_cache = None

    def remove_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        Select(wd.find_element(By.NAME, "group")).select_by_value(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element(By.NAME, "remove").click()

    def remove_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contacts_page()
        self.remove_contact_from_group_by_id(contact_id, group_id)
        self.open_contacts_page()
        self.contact_cache = None
