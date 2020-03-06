# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserGroups(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_create_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\" Создать \"]")

    def get_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"name\"]")

    def get_save_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\" Создать \"]")

    def get_search(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "userGroupGridState_smart-search-input")

    # ACTION ELEMENTS
    def click_create_btn(self):
        el = self.get_create_btn()
        el.click()

    def type_name(self, text):
        name = self.get_name()
        name.clear()
        name.send_keys(text)

    def click_save_btn(self):
        el = self.get_save_btn()
        el.click()

    def remove_companies(self, text):
        search_element = self.get_search()
        self.app.base_page.remove_element_in_table(text, search_element)
