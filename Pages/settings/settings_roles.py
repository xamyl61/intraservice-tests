# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By


class SettingsRoles(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_create_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\"Создать\"]")

    def get_create_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@placeholder=\"Наименование\"]")

    def get_create_description(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//textarea[@placeholder=\"Описание\"]")

    def get_type_role(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//span[@class=\"k-select\"]")

    def get_type_role_item(self, role_type):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"k-popup k-list-container k-reset multiselectpopup\"]"
                                         "//*[text()=\"" + role_type + "\"]")

    def get_radio_by_label_text(self, label):
        wd = self.app.wd
        return wd.find_element(By.XPATH,
                               "//label[text()=\"" + label[0] + "\"]//following::label[text()=\"" + label[1] + "\"]")

    def get_save(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button//*[@class=\"k-icon k-i-save\"]")

    def get_table_cell_name(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//tr//td[3]")

    def get_search(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "Roles_smart-search-input")

    def get_role_in_table(self, role_name):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//table//tr//td[text()=\"" + role_name + "\"]")

    def get_remove_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"buttons\"]//button[contains(text(), \"Удалить\")]")

    def get_roles(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//table//tbody//tr//td[3]")

    # ACTIONS WITH ELEMENTS
    def click_create_btn(self):
        time.sleep(2)
        self.get_create_btn().click()

    def type_name(self, name_text):
        name = self.get_create_name()
        name.clear()
        name.send_keys(name_text)

    def type_description(self, name_text):
        name = self.get_create_description()
        name.clear()
        name.send_keys(name_text)

    def choose_role(self, role_type):
        self.get_type_role().click()
        time.sleep(3)
        self.get_type_role_item(role_type).click()

    def choose_radio_by_label_text(self, label):
        self.get_radio_by_label_text(label).click()

    def click_save_new_role_btn(self):
        self.get_save().click()
        time.sleep(3)

    def remove_role(self, role_list):
        for role in role_list:
            element = self.get_role_in_table(role)
            checkbox = element.find_element_by_xpath(
                ".//ancestor::tr//td[1]//label")
            checkbox.click()
        self.get_remove_btn().click()

    # ASSERTS
    def check_value_in_list(self, text):
        el_list = self.get_table_cell_name()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text in el_texts, "Искомый текст не найден в списке."

    def check_roles_was_removed(self, role_list):
        for role in role_list:
            el_list = self.get_roles()
            el_texts = self.app.helpers.create_list_text(el_list)
            assert role not in el_texts








