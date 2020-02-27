# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By


class Tasks:

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_tasks_line_name(self, text):
        wd = self.app.wd
        return wd.find_element_by_xpath("//table[@class=\"k-grid-table\"]//*[text()=\"" + text + "\"]")

    def get_tasks_line_names(self):
        wd = self.app.wd
        return wd.find_elements_by_xpath("//table[@class=\"k-grid-table\"]//tr//td[3]"
                                         "//span[@class=\"tasklistgrid_task\"]")

    def get_action_btn(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//button[@class=\"k-button\"]//span[text()=\"Действия\"]")

    def get_action_btn_remove(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//ul[@class=\"k-list k-reset\"]//li[text()=\" Удалить \"]")

    def get_modal_yes_btn(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//button[@class=\"k-button ng-star-inserted\"][text()=\"Да\"]")

    # ACTIONS WITH ELEMENTS
    def choose_task_in_table(self, text):
        element = self.get_tasks_line_name(text)
        parent_line = element.find_element_by_xpath(".//ancestor::tr"
                                                    "//label[@class=\"k-checkbox-label\"]")
        parent_line.click()

    def click_action_btn_remove(self):
        self.get_action_btn().click()
        self.get_action_btn_remove().click()
        self.get_modal_yes_btn().click()
        time.sleep(10)

    # ASSERTS
    def check_name_was_removed(self, text):
        el_list = self.get_tasks_line_names()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text not in el_texts


