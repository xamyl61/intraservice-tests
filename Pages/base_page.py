# -*- coding: utf-8 -*-
import time
from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class BasePage(object):

    def __init__(self, app):
        self.app = app

    url = None

    def scroll_page_to_bottom(self):
        wd = self.app.wd
        prev_window_height = 0
        sleep(1)
        if wd.execute_script("return document.documentElement.scrollHeight>document.documentElement.clientHeight;"):
            while wd.execute_script("return document.documentElement.scrollHeight;") > prev_window_height:
                prev_window_height = wd.execute_script("return document.documentElement.scrollHeight;")
                wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(1)

    def refresh_page(self):
        wd = self.app.wd
        wd.refresh()
        sleep(6)

    def open_new_tab(self):
        wd = self.app.wd
        wd.execute_script("window.open('');")

    def switch_tab(self, tab):
        wd = self.app.wd
        wd.switch_to_window(wd.window_handles[tab - 1])

    def close_tab(self):
        wd = self.app.wd
        wd.close()

    def get_current_date_time(self):
        now = datetime.now()
        return now.strftime("%H_%M_%S")

    def click_tab(self, tab_text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//li/span[text()=\"" + tab_text + "\"]").click()

    def type_and_choose_text(self, element, text):
        wd = self.app.wd
        element.send_keys(text)
        time.sleep(3)
        wd.find_element(By.XPATH, "//div[contains(@class, \"k-popup\")]//*[text()=\"" + text + "\"]").click()

    def type_in_search_filter(self, element, text):
        element.send_keys(text)
        time.sleep(1)
        element.send_keys(Keys.RETURN)
        time.sleep(4)

    def is_element_focus(self, element):
        wd = self.app.wd
        return element == wd.switch_to.active_element

    def click_popup_yes_btn(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[@class=\"k-button ng-star-inserted\"][text()=\"Да\"]").click()
        time.sleep(4)

    def click_remove_modal_yes_btn(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//button[text()=\"Удалить\"]")
        element.click()

    # Find and remove from table
    def get_element_after_search(self, text):
        wd = self.app.wd
        return wd.find_element(By.XPATH,
                               "//div[@class=\"k-grid-aria-root\"]//table//tbody//tr//td"
                               "//*[text()=\"" + text + "\"]")

    def get_no_record_text(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@class=\"k-grid-norecords\"]")

    def get_remove_btn(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*//button[contains(text(), \"Удалить\")]")

    def type_search(self, text, search_element):
        search_element.clear()
        search_element.send_keys(text)
        time.sleep(2)
        search_element.send_keys(Keys.RETURN)
        time.sleep(3)

    def remove_element_in_table(self, text, search_element):
        self.type_search(text, search_element)
        element = self.get_element_after_search(text)
        checkbox = element.find_element_by_xpath(
            ".//ancestor::tr//td[1]//label")
        checkbox.click()
        self.get_remove_btn().click()
        time.sleep(3)
        self.click_popup_yes_btn()

    def check_element_was_removed(self, ):
        el_texts = self.get_no_record_text().text
        assert el_texts == "Нет доступных записей"

    def check_remove_notification_message(self):
        wd = self.app.wd
        el = wd.find_element(By.CSS_SELECTOR, ".k-notification-container-animating "
                                              ".k-notification-success .k-notification-content div div")
        assert el.text == "Успешно удалено"

    def check_success_notification_message(self):
        wd = self.app.wd
        el = wd.find_element(By.CSS_SELECTOR, ".k-notification-group")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", el.get_attribute('innerHTML'))
        # return wd.find_element(By.XPATH, "//*[contains(text(), \"Выполнено успешно\")]")
        # print("!!!!!!!")
        # print("el.text: ", el.text)
        # print("!!!!!!!")
        # assert el.text == "Выполнено успешно"
        TIMEOUT = 5
        WebDriverWait(self.app.wd, TIMEOUT).until(
            EC.text_to_be_present_in_element(
                [By.CSS_SELECTOR, ".k-notification-success .k-notification-content div div"],
                "Выполнено успешно"))













