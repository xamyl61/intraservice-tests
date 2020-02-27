# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsServices(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_create_service(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector(".root-title button")

    def get_service_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"name\"]")

    def get_services_name(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//input[@formcontrolname=\"name\"]")

    def get_confirm_service_name(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("button.tree-btn.submit-btn")

    def get_created_service_by_name(self, service_name):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//span[text()=\"" + service_name + "\"]")

    def get_service_card_tab(self, tab_text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//li/span[text()=\"" + tab_text + "\"]")

    def get_search_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@placeholder=\"Введите имя...\"]")

    def get_save_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\"Сохранить\"]")

    def get_radio_btn(self, radio_text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//label[text()=\"" + radio_text + "\"]")

    def get_accept_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[@class=\"k-button ng-star-inserted\"][text()=\"Да\"]")

    def get_checkbox(self, checkbox_text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//label[text()=\"" + checkbox_text + "\"]")

    # ACTIONS WITH ELEMENTS
    def click_create_service(self):
        wd = self.app.wd
        time.sleep(4)
        wait = WebDriverWait(wd, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.root-title button')))
        element.click()

    def type_service_name(self, text):
        name = self.get_service_name()
        name.clear()
        name.send_keys(text)
        name.send_keys(Keys.RETURN)
        time.sleep(3)

    def click_confirm_create_service(self):
        self.get_confirm_service_name().click()
        time.sleep(3)

    def open_created_service(self, service_name):
        self.get_created_service_by_name(service_name).click()
        time.sleep(3)

    def click_service_card_tab(self, tab_text):
        self.get_service_card_tab(tab_text).click()

    def type_search_name(self, text):
        search = self.get_search_name()
        search.clear()
        search.send_keys(text)
        time.sleep(3)
        self.get_service_name().click()
        time.sleep(1)

    def click_save_btn(self):
        self.get_save_btn().click()

    def click_radio_btn(self, radio_text):
        self.get_radio_btn(radio_text).click()

    def click_accept_btn(self):
        self.get_accept_btn().click()
        time.sleep(1)

    def click_checkbox(self, checkbox_text):
        self.get_radio_btn(checkbox_text).click()

    def remove_service_from_tree(self, text):
        element = self.get_created_service_by_name(text)
        remove_icon = element.find_element_by_xpath(
            ".//ancestor::div[contains(@class, \"tree-title\")]//button[contains(@class, \"delete-btn\")]")
        remove_icon.click()
        time.sleep(3)

    # ASSERTS
    def check_service_was_removed(self, text):
        el_list = self.get_services_name()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text not in el_texts











