# -*- coding: utf-8 -*-


class Helpers:

    def __init__(self, app):
        self.app = app

    def create_list_text(self, list_elements):
        text_list = []
        for element in list_elements:
            text_list.append(element.text)
        return text_list

    # def check_value_in_list(self, text, el_texts):
    #     assert text in el_texts, "Искомый текст не найден в списке."