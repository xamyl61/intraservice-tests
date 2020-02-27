# -*- coding: utf-8 -*-
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsRulesWorkflow(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_new_rule(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\"Правило назначения Бизнес-процесса\"]")

    def get_service_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@placeholder=\"Введите сервис\"]")

    def get_business_process(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".k-dropdown-wrap.k-state-default .k-select")

    def get_dropdown_item(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//ul//li//span[text()=\"" + text + "\"]")

    def get_dropdown_search(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".k-list-filter input.k-textbox")

    def get_save_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[@class=\"k-button-icon k-button k-primary\"]")

    def get_search_filter(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "RulesUseWorkflow_smart-search-input")

    def get_search_results(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//li//span")

    def get_no_record_text(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@class=\"k-grid-norecords\"]")

    def get_service_by_name(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//li//span[text()=\"" + text + "\"]")

    def get_remove_rule_btn(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//button[@class=\"k-button-icontext k-button\"][text()=\"Удалить \"]")

    # ACTIONS WITH ELEMENTS
    def click_new_rule(self):
        self.get_new_rule().click()

    def type_service_name(self, text):
        service = self.get_service_name()
        service.clear()
        service.send_keys(text)
        time.sleep(2)
        self.get_dropdown_item(text).click()

    # def type_service_name(self, text):
    #     wd = self.app.wd
    #     service = self.get_service_name()
    #     service.clear()
    #     service.send_keys(text)
    #     ActionChains(wd).key_down(Keys.ARROW_DOWN) \
    #         .key_up(Keys.ARROW_DOWN) \
    #         .key_down(Keys.ENTER) \
    #         .key_up(Keys.ENTER) \
    #         .perform()
    #     time.sleep(3)

    def choose_business_process_item(self, text):
        wd = self.app.wd
        self.get_business_process().click()
        ActionChains(wd).send_keys(text)\
            .key_down(Keys.ARROW_DOWN) \
            .key_up(Keys.ARROW_DOWN) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.ENTER) \
            .perform()
        time.sleep(3)

    def click_save_btn(self):
        self.get_new_rule().click()
        time.sleep(2)

    def type_search_filter(self, text):
        elem = self.get_search_filter()
        elem.clear()
        elem.send_keys(text)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(4)

    def choose_rule_in_table(self, text):
        element = self.get_service_by_name(text)
        checkbox = element.find_element_by_xpath(
            ".//ancestor::tr//td[1]//label")
        checkbox.click()

    def click_remove_rule_btn(self):
        self.get_remove_rule_btn().click()
        time.sleep(4)

    # Asserts
    def check_search_results(self, text):
        el_list = self.get_search_results()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text in el_texts, "Искомый текст не найден в списке."

    def check_ruele_was_removed(self):
        el_texts = self.get_no_record_text().text
        assert el_texts == "No records available."

