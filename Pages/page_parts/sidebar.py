# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class Sidebar(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_sidebar_item(self, sidebar_item):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class=\"menu-title\"][text()=\"" + sidebar_item + "\"]")

    # ACTIONS WITH ELEMENTS
    def click_sidebar_item(self, sidebar_item):
        self.get_sidebar_item(sidebar_item).click()

    # ASSERTS
    def check_menu_load(self, sidebar_items):
        for item in sidebar_items:
            self.get_sidebar_item(item)
        print("Проверка - боковое меню загрузилось.")
