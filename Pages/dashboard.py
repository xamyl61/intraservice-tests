# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By


class Dashboard:

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_create_task(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".btn.create-task")

    def get_created_service(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"service-info_wrap\"]//p[text()=\"" + text + " " + "\"]")

    def get_task_name_input(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//textarea[@class=\"task-name creation\"]")

    def get_save_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//button//span[text()=\"Сохранить\"]")

    def get_created_tasks(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//table//tbody//tr//td[3]//span")

    def get_logout_btn(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".button_exit")

    # ACTIONS WITH ELEMENTS
    def click_create_task(self):
        self.get_create_task().click()

    def open_created_service(self, text):
        self.get_created_service(text).click()

    def type_task_name(self, text):
        username = self.get_task_name_input()
        username.clear()
        username.send_keys(text)

    def click_save_btn(self):
        self.get_save_btn().click()

    def click_logout_btn(self):
        self.get_logout_btn().click()

    # ASSERTS
    def check_cursor_in_name_field(self):
        element = self.get_task_name_input()
        self.app.base_page.is_element_focus(element)

    def check_created_task(self, text):
        el_list = self.get_created_tasks()
        el_texts = self.app.helpers.create_list_text(el_list)
        assert text in el_texts, "Искомый текст не найден в списке."




