# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsUsersClients(object):

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

    def get_companies(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//span[text()=\"Выберите компанию...\"]")

    def get_companies_search(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@class=\"k-textbox ng-untouched ng-pristine ng-valid\"]")

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

    def get_table_cell_name(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//tr//td[3]")

    def get_table_cell_secondname(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//tr//td[4]")

    def get_table_cell_lastname(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//tr//td[5]")

    def get_table_cell_email(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//tr//td[6]")

    def get_search(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "clientGridState_smart-search-input")

    def get_clear_search_icon(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".clear-btn")

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

    def type_companies(self, text):
        self.get_companies().click()
        search = self.get_companies_search()
        search.clear()
        search.send_keys(text)
        time.sleep(4)
        search.send_keys(Keys.RETURN)

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
        # time.sleep(3)

    def remove_client(self, text):
        search_element = self.get_search()
        self.app.base_page.remove_element_in_table(text, search_element)

    def type_search_filter(self, text):
        element = self.get_search()
        element.clear()
        self.app.base_page.type_in_search_filter(element, text)

    def click_table_cell_name(self):
        self.get_table_cell_name()[0].click()

    def click_clear_search(self):
        el = self.get_search()
        el.send_keys(" ")
        self.get_clear_search_icon().click()

    # ASSERTS
    def check_value_in_list(self, text):
        el_list = self.get_table_cell_name()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text in el_texts, "Искомый текст не найден в списке."

    def check_changed_fields(self, name, second_name, last_name, email):
        name_val = self.get_table_cell_name()[0].text
        second_name_val = self.get_table_cell_secondname()[0].text
        last_name_val = self.get_table_cell_lastname()[0].text
        email_val = self.get_table_cell_email()[0].text

        assert name_val == name
        assert second_name_val == second_name
        assert last_name_val == last_name
        assert email_val == email













