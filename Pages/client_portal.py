# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By


class ClientPortal:

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_reset_filter_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"left_panel\"]//button[@title=\"Сбросить фильтр заявок\"]")

    def get_username(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".username")

    def get_first_row_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//table[@class=\"k-grid-table\"]//tr[1]//td[3]//span")

    def get_first_row_executor(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//table[@class=\"k-grid-table\"]//tr[1]//td[6]//span")

    def get_text_editor(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".ckeditor-wrapper .cke_wysiwyg_div")

    def get_save_editor_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"save-bottom-buttons-wrapper\"]//div[@class=\"button\"]")

    def get_comment(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"comment single\"]")

    def get_logout_btn(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".exit-button")

    def click_logout_btn(self):
        self.get_logout_btn().click()

    # ACTIONS WITH ELEMENTS
    def type_text_editor(self, text):
        # self.get_text_editor().click
        text_editor = self.get_text_editor()
        text_editor.send_keys(text)

    def click_first_row_name(self):
        self.get_first_row_name().click()

    def click_reset_filter_btn(self):
        self.get_reset_filter_btn().click()

    def click_save_editor_btn(self):
        self.get_save_editor_btn().click()
        time.sleep(6)

    # ASSERTS
    def check_url(self):
        wd = self.app.wd
        self.get_reset_filter_btn()
        current_url = wd.current_url
        assert current_url == self.app.base_url + "task/list"

    def check_executor_in_results(self, text):
        title = self.get_first_row_name().text
        executor = self.get_first_row_executor().text
        username = self.get_username().text
        assert text + username == title + executor

    def check_comment_added(self, text):
        comment_text = self.get_comment().text
        assert text == comment_text








