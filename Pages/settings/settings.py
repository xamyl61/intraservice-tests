# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Settings(object):

    def __init__(self, app):
        self.app = app

    # FIND ELEMENTS
    def get_setting_nav(self, nav_item):
        wd = self.app.wd
        return wd.find_element(By.XPATH,
                               "//*[@class=\"k-pane-static k-pane k-scrollable\"]//*[text()=\"" + nav_item + "\"]")

    def click_menu_by_text(self, nav_items):
        for item in nav_items:
            self.get_setting_nav(item).click()
