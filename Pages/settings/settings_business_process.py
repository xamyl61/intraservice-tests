# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsBusinessProcess(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_search_filter(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "workflows_smart-search-input")

    def get_search_results(self, text):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//li//span[text()=\"" + text + "\"]")

    def get_search_text(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//table[@class=\"k-grid-table\"]//td[text()=\"" + text + "\"]")

    def get_searched_executor(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//table[@class=\"ng-star-inserted\"]//tr//td[3]//li[text()=\"" + text + "\"]")

    def get_executors_names(self):
        wd = self.app.wd
        return wd.find_elements_by_xpath("//table[@class=\"ng-star-inserted\"]//tr//td[3]//li")

    def get_remove_executors_btn(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//button[@class=\"k-button-icontext k-button\"][text()=\"Удалить\"]")

    # ACTIONS WITH ELEMENTS
    def type_search_filter(self, text):
        elem = self.get_search_filter()
        elem.send_keys(text)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(4)

    def click_search_text(self, text):
        self.get_search_text(text).click()
        time.sleep(2)

    def choose_executor_in_table(self, text):
        element = self.get_searched_executor(text)
        checkbox = element.find_element_by_xpath(
            ".//ancestor::tr//td[1]//label")
        checkbox.click()

    def click_remove_executors_btn(self):
        self.get_remove_executors_btn().click()
        time.sleep(4)

    # Asserts
    def check_search_results(self, text):
        el_list = self.get_search_results(text)
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text in el_texts, "Искомый текст не найден в списке."

    def check_executor_was_removed(self, text):
        el_list = self.get_executors_names()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text not in el_texts

