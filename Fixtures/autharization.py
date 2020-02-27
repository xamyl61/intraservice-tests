# -*- coding: utf-8 -*-


class AuthorizationHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.login_page.open_page()
        self.app.login_page.type_username(username)
        self.app.login_page.type_password(password)
        self.app.login_page.click_confirm_btn()

    def logout(self):
        self.app.login_page.click_logout_btn()

