# -*- coding: utf-8 -*-


class Helpers:

    def __init__(self, app):
        self.app = app

    def create_list_text(self, list_elements):
        text_list = []
        for element in list_elements:
            text_list.append(element.text)
        return text_list
