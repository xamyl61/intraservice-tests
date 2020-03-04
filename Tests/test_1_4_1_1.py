# -*- coding: utf-8 -*-
import time


def test_1_4_1_1(app):
    current_time = "id_1.4.1.1"
    app.authorization.login(app.config["LOGIN"], app.config["PASSWORD"])

    # Проверка создание роли клиента
    app.wd.get(app.base_url + "settings/roles")
    app.settings_roles.click_create_btn()
    app.settings_roles.type_name("РольКл1_" + current_time)
    app.settings_roles.type_description("это_описание_роли_клиента_Автотест")
    app.settings_roles.choose_role("Клиент")
    app.settings_roles.choose_radio_by_label_text(("Заявки: ", "Только свои"))
    app.settings_roles.choose_radio_by_label_text(("База знаний: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("Пользователи: ", "Только свой профиль"))
    app.settings_roles.click_save_new_role_btn()
    app.base_page.refresh_page()
    app.settings_roles.check_value_in_list("РольКл1_" + current_time)

    # Создание компании
    app.wd.get(app.base_url + "settings/clientcompanies")
    app.settings_clientcompanies.click_create_btn()
    app.settings_clientcompanies.type_name("КомпанияКлиента1_" + current_time)
    app.settings_clientcompanies.type_description("Описание_" + current_time)
    app.settings_clientcompanies.type_address("Адрес_" + current_time)
    app.settings_clientcompanies.type_web("www.testcompany.test")
    app.settings_clientcompanies.type_email("tes@emailautomated.test")
    app.settings_clientcompanies.type_additional_info("Некоторая дополнительная информация")
    app.settings_clientcompanies.type_tags("тег_" + current_time)
    app.settings_clientcompanies.type_domen("www")
    app.settings_clientcompanies.type_employes_count("2")
    app.settings_clientcompanies.click_save_btn()

    # # Создание клиента 1
    app.wd.get(app.base_url + "settings/users/clients")
    app.settings_usersclients.click_create_btn()
    app.settings_usersclients.type_lastname("ФамилияКл1" + current_time)
    app.settings_usersclients.type_firstname("ИмяКл1")
    app.settings_usersclients.type_middlename("ОтчествоКл1")
    app.settings_usersclients.type_companies("КомпанияКлиента1_" + current_time)
    app.settings_usersclients.type_email("k1_" + current_time + "@gmail.com")
    app.settings_usersclients.type_role("РольКл1_" + current_time)
    app.settings_usersclients.type_password("1")
    app.settings_usersclients.type_password_confirmation("1")
    app.settings_usersclients.click_save_btn()

    # Создание клиента 2
    app.settings_usersclients.click_create_btn()
    app.settings_usersclients.type_lastname("ФамилияКл2" + current_time)
    app.settings_usersclients.type_firstname("ИмяКл2")
    app.settings_usersclients.type_middlename("ОтчествоКл2")
    app.settings_usersclients.type_companies("КомпанияКлиента1_" + current_time)
    app.settings_usersclients.type_email("k2_" + current_time + "@gmail.com")
    app.settings_usersclients.type_role("РольКл1_" + current_time)
    app.settings_usersclients.type_password("1")
    app.settings_usersclients.type_password_confirmation("1")
    app.settings_usersclients.click_save_btn()
    app.base_page.refresh_page()

    # Проверка что клиент создался
    app.settings_usersclients.type_search_filter("ФамилияКл1" + current_time)
    app.settings_usersclients.check_value_in_list("ФамилияКл1" + current_time)

    # Изменение клиента 1
    app.settings_usersclients.click_table_cell_name()
    app.settings_usersclients.type_lastname("ФамилияКл1" + current_time + "_изм")
    app.settings_usersclients.type_firstname("ИмяКл1" + "_изм")
    app.settings_usersclients.type_middlename("ОтчествоКл1" + "_изм")
    app.settings_usersclients.type_email("k1_" + current_time + "changed" + "@gmail.com")
    app.settings_usersclients.click_save_btn()
    app.base_page.refresh_page()

    app.settings_usersclients.click_clear_search()
    app.settings_usersclients.type_search_filter("ФамилияКл1" + current_time + "_изм")
    app.settings_usersclients.check_changed_fields("ФамилияКл1" + current_time + "_изм",
                                                   "ИмяКл1" + "_изм",
                                                   "ОтчествоКл1" + "_изм",
                                                   "k1_" + current_time + "changed" + "@gmail.com")

    # Удаление клиентов
    app.settings_usersclients.click_clear_search()
    app.settings_usersclients.remove_client("ФамилияКл1" + current_time + "_изм")
    app.base_page.check_remove_notification_message()
    app.base_page.refresh_page()
    app.base_page.check_element_was_removed()

    app.settings_usersclients.click_clear_search()
    app.settings_usersclients.remove_client("ФамилияКл2" + current_time)
    app.base_page.check_remove_notification_message()
    app.base_page.refresh_page()
    app.base_page.check_element_was_removed()

    # Удаление компании
    app.wd.get(app.base_url + "settings/clientcompanies")
    app.settings_clientcompanies.remove_companies("КомпанияКлиента1_" + current_time)
    app.base_page.check_remove_notification_message()
    app.base_page.refresh_page()
    app.base_page.check_element_was_removed()

    # Удаление роли сотрудника
    app.wd.get(app.base_url + "settings/roles")
    app.settings_roles.remove_role([
        "РольКл1_" + current_time])
    app.base_page.click_popup_yes_btn()
    app.base_page.refresh_page()
    app.settings_roles.check_roles_was_removed([
        "РольКл1_" + current_time])

    app.authorization.logout()
