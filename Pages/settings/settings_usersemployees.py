# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsUsersEmployees(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_create_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\"Создать\"]")

    def get_lastname(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"lastName\"]")

    def get_firstname(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"firstName\"]")

    def get_middlename(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"middleName\"]")

    def get_email(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"email\"]")

    def get_role(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH,
                               "//span[text()=\"Роль\"]//following::kendo-dropdownlist//span[@class=\"k-input\"]")

    def get_role_search(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@class=\"k-animation-container k-animation-container-shown\"]//input")

    def get_password(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"password\"]")

    def get_password_confirmation(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"passwordConfirmation\"]")

    def get_save_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[@class=\"k-button-icon k-button k-primary\"]")

    def get_search(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "employeeGridState_smart-search-input")

    def get_element_after_search(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH,
                               "//div[@class=\"k-grid-aria-root\"]//table//tbody//tr//td"
                               "//*[text()=\"" + text + "\"]")

    def get_no_record_text(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@class=\"k-grid-norecords\"]")

    def get_remove_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"buttons\"]//button[text()=\" Удалить \"]")

    # ACTIONS WITH ELEMENTS
    def click_create_btn(self):
        time.sleep(2)
        self.get_create_btn().click()

    def type_lastname(self, text):
        name = self.get_lastname()
        name.clear()
        name.send_keys(text)

    def type_firstname(self, text):
        name = self.get_firstname()
        name.clear()
        name.send_keys(text)

    def type_middlename(self, text):
        name = self.get_middlename()
        name.clear()
        name.send_keys(text)

    def type_middlename(self, text):
        name = self.get_middlename()
        name.clear()
        name.send_keys(text)

    def type_email(self, text):
        name = self.get_email()
        name.clear()
        name.send_keys(text)

    def type_role(self, text):
        self.get_role().click()
        search = self.get_role_search()
        search.clear()
        search.send_keys(text)
        time.sleep(2)
        search.send_keys(Keys.RETURN)

    def type_password(self, text):
        name = self.get_password()
        name.clear()
        name.send_keys(text)

    def type_password_confirmation(self, text):
        name = self.get_password_confirmation()
        name.clear()
        name.send_keys(text)

    def click_save_btn(self):
        self.get_save_btn().click()
        time.sleep(3)

    def type_search(self, text):
        search = self.get_search()
        search.clear()
        search.send_keys(text)
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        time.sleep(3)

    def choose_rule_in_table(self, text):
        element = self.get_element_after_search(text)
        checkbox = element.find_element_by_xpath(
            ".//ancestor::tr//td[1]//label")
        checkbox.click()

    def click_remove_btn(self):
        self.get_remove_btn().click()

    # ASSERTS
    def check_value_in_list(self, text):
        el_list = self.get_table_cell_name()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text in el_texts, "Искомый текст не найден в списке."

    def check_employee_was_removed(self):
        el_texts = self.get_no_record_text().text
        assert el_texts == "No records available."










