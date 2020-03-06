# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsClientCompanies(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_create_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\" Создать \"]")

    def get_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"name\"]")

    def get_description(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//textarea[@formcontrolname=\"description\"]")

    def get_address(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"address\"]")

    def get_web(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"web\"]")

    def get_phone_number(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@title=\"Номер телефона\"]")

    def get_email(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"email\"]")

    def get_additional_info(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@formcontrolname=\"additionalInfo\"]")

    def get_tags(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//span[text()=\"Теги\"]//following::app-edit-tags//input")

    def get_domen(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//span[text()=\"Домен \"]//following::kendo-multiselect//input")

    def get_employes_count(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//span[text()=\"Число сотрудников \"]//following::label//input")

    def get_save_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\"Сохранить\"]")

    def get_table_cell_name(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//tr//td[3]")

    def get_search(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "clientCompanyGridState_smart-search-input")

    def get_sorted_id(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@class=\"k-grid-aria-root\"]//thead//th[2]")

    # ACTIONS WITH ELEMENTS
    def click_create_btn(self):
        time.sleep(3)
        self.get_create_btn().click()

    def type_name(self, name_text):
        name = self.get_name()
        name.clear()
        name.send_keys(name_text)

    def type_description(self, description):
        name = self.get_description()
        name.clear()
        name.send_keys(description)

    def type_address(self, address):
        name = self.get_address()
        name.clear()
        name.send_keys(address)

    def type_web(self, web):
        name = self.get_web()
        name.clear()
        name.send_keys(web)

    def type_phone_number(self, phone_number):
        name = self.get_phone_number()
        name.clear()
        name.send_keys(phone_number)

    def type_email(self, email):
        name = self.get_email()
        name.clear()
        name.send_keys(email)

    def type_additional_info(self, additional_info):
        name = self.get_additional_info()
        name.clear()
        name.send_keys(additional_info)

    def type_tags(self, tags):
        name = self.get_tags()
        name.clear()
        name.send_keys(tags)
        name.send_keys(Keys.RETURN)

    def type_domen(self, domen):
        name = self.get_domen()
        name.clear()
        name.send_keys(domen)
        name.send_keys(Keys.RETURN)

    def type_employes_count(self, employes_count):
        name = self.get_employes_count()
        name.clear()
        name.send_keys(employes_count)

    def click_save_btn(self):
        self.get_save_btn().click()
        # time.sleep(3)

    def remove_companies(self, text):
        search_element = self.get_search()
        self.app.base_page.remove_element_in_table(text, search_element)

    def click_sorted_id(self):
        el = self.get_sorted_id()
        el.click()

    # ASSERTS
    def check_value_in_list(self, text):
        el_list = self.get_table_cell_name()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text in el_texts, "Искомый текст не найден в списке."




