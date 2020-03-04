# -*- coding: utf-8 -*-
from selenium import webdriver

from Fixtures.helpers import Helpers
from Fixtures.autharization import AuthorizationHelper

from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from Pages.page_parts.sidebar import Sidebar
from Pages.settings.settings import Settings
from Pages.settings.settings_roles import SettingsRoles
from Pages.settings.settings_clientcompanies import SettingsClientCompanies
from Pages.settings.settings_usersclients import SettingsUsersClients
from Pages.settings.settings_usersemployees import SettingsUsersEmployees
from Pages.settings.settings_services import SettingsServices
from Pages.settings.settings_rules_workflow import SettingsRulesWorkflow
from Pages.settings.settings_business_process import SettingsBusinessProcess
from Pages.settings.settings_business_process_card import SettingsBusinessProcessCard
from Pages.dashboard import Dashboard
from Pages.client_portal import ClientPortal
from Pages.tasks import Tasks
from Pages.settings.usergroups import UserGroups


class Application:

    def __init__(self, driver, settings):

        # self.wd = webdriver.Chrome("/Users/alexanderonishchenko/Documents/intraservice-tests/chromedriver_mac64")
        self.wd = driver
        # self.wd.implicitly_wait(30)
        # self.wd.maximize_window()

        self.helpers = Helpers(self)
        self.authorization = AuthorizationHelper(self)
        self.base_page = BasePage(self)
        self.login_page = LoginPage(self)
        self.sidebar = Sidebar(self)
        self.settings = Settings(self)
        self.settings_roles = SettingsRoles(self)
        self.settings_clientcompanies = SettingsClientCompanies(self)
        self.settings_usersclients = SettingsUsersClients(self)
        self.settings_usersemployees = SettingsUsersEmployees(self)
        self.settings_services = SettingsServices(self)
        self.settings_rules_workflow = SettingsRulesWorkflow(self)
        self.business_process = SettingsBusinessProcess(self)
        self.settings_business_process_card = SettingsBusinessProcessCard(self)
        self.dashboard = Dashboard(self)
        self.client_portal = ClientPortal(self)
        self.tasks = Tasks(self)
        self.usergroups = UserGroups(self)

        self.base_url = 'https://is5.intra5.ru/'
        self.settings = settings


    # def destroy(self):
    #     current_time = self.base_page.get_current_date_time()
    #     f = open("../browser_logs/browser_log_{}.txt".format(current_time), "w+")
    #     for entry in self.wd.get_log('browser'):
    #         f.write("{}\r\n".format(entry))
    #     f.close()
    #     self.wd.save_screenshot("../screenshots/screenshot_{}.png".format(current_time));
    #     self.wd.quit()

