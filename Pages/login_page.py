# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    # FIND ELEMENTS
    def get_username(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "Username")

    def get_password(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "Password")

    def get_confirm_btn(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//button[@value=\"login\"]")

    def get_logout_btn(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".exit-button")

    # ACTIONS WITH ELEMENTS
    def type_username(self, username_text):
        username = self.get_username()
        username.clear()
        username.send_keys(username_text)

    def type_password(self, password_text):
        password = self.get_password()
        password.clear()
        password.send_keys(password_text)

    def click_confirm_btn(self):
        self.get_confirm_btn().click()

    def click_logout_btn(self):
        self.get_logout_btn().click()





