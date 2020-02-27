# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsBusinessProcessCard(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_assign_executor_group_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[text()=\"Назначения Исполнителя/Группы\"]")

    def get_services(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@placeholder=\"Введите сервис\"]")

    def get_assignment(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//input[@placeholder=\"нет назначения\"]")

    def get_save_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button[@class=\"k-button-icon k-button k-primary\"]")

    def get_search_filter(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "RulesExecutor_smart-search-input")

    def get_search_text(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//table[@class=\"k-grid-table\"]//td[text()=\"" + text + "\"]")

    def get_search_results_statuses(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//table//tbody//tr//td[3]//li")

    def get_search_results_executor(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div[@class=\"k-grid-aria-root\"]//table//tbody//tr//td[4]//span[2]")

    # ACTIONS WITH ELEMENTS
    def type_search_filter(self, text):
        element = self.get_search_filter()
        self.app.base_page.type_in_search_filter(element, text)

    def click_assign_executor_group_btn(self):
        self.get_assign_executor_group_btn().click()

    def choose_business_process(self, text):
        wd = self.app.wd
        element = self.get_services()
        wd = self.app.wd
        element.send_keys(text)
        time.sleep(3)
        wd.find_element(By.XPATH, "//div[contains(@class, \"k-popup\")]//*[text()=\"" + text + "\"]").click()
        services = wd.find_elements(By.XPATH,
                                    "//div[@class=\"col-md-6 padding_left0\"][1]"
                                    "//div[@class=\"k-multiselect-wrap k-floatwrap\"]//ul[@class=\"k-reset\"]")
        if len(services) == 0:
            self.choose_business_process(text)

    def choose_assignment(self, text):
        field = self.get_assignment()
        field.clear()
        field.send_keys(text)
        time.sleep(8)
        field.send_keys(Keys.ENTER)

    def click_save_btn(self, text):
        self.get_save_btn().click()
        time.sleep(3)
        wd = self.app.wd
        elem = wd.find_elements(By.XPATH,
                                "//span[text()=\" Нужно выбрать хотя бы одного исполнителя или группу исполнителей \"]")
        if len(elem) != 0:
            self.choose_assignment(text)
        self.get_save_btn().click()

    def click_search_text(self, text):
        self.get_search_text(text).click()

    # ASSERTS
    def check_search_results(self, text):
        time.sleep(4)
        statuses = self.get_search_results_statuses()
        executor = self.get_search_results_executor()
        statuses_lists = self.app.helpers.create_list_text(statuses)
        executor_lists = self.app.helpers.create_list_text(executor)
        result = [tuple(tup) for tup in zip(statuses_lists, executor_lists)]
        assert text in result, "Искомый текст не найден в списке."

