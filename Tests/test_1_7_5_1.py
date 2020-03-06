# -*- coding: utf-8 -*-
import time


def test_1_7_5_1(app):
    current_time = "id_1.7.5.1"
    app.authorization.login(app.config["LOGIN"], app.config["PASSWORD"])

    # # Проверка создание роли клиента
    app.wd.get(app.base_url + "settings/roles")
    app.settings_roles.click_create_btn()
    app.settings_roles.type_name("Клиентская_" + current_time)
    app.settings_roles.type_description("это_описание_роли_клиента_Автотест")
    app.settings_roles.choose_role("Клиент")
    app.settings_roles.choose_radio_by_label_text(("Заявки: ", "Только свои"))
    app.settings_roles.choose_radio_by_label_text(("База знаний: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("Пользователи: ", "Только свой профиль"))
    app.settings_roles.click_save_new_role_btn()
    app.base_page.check_notification_success("Выполнено успешно")
    app.base_page.refresh_page()
    app.settings_roles.check_value_in_list("Клиентская_" + current_time)

    # Проверка создание роли исполнителя
    app.wd.get(app.base_url + "settings/roles")
    app.settings_roles.click_create_btn()
    app.settings_roles.type_name("Исполнительская_" + current_time)
    app.settings_roles.type_description("это_описание_роли_исполнителя_Автотест")
    app.settings_roles.choose_role("Сотрудник")
    app.settings_roles.choose_radio_by_label_text(("Заявки: ", "Только свои"))
    app.settings_roles.choose_radio_by_label_text(("Активы: ", "Свои"))
    app.settings_roles.choose_radio_by_label_text(("База знаний: ", "Просмотр"))
    app.settings_roles.choose_radio_by_label_text(("Сотрудники и группы: ", "Просмотр"))
    app.settings_roles.choose_radio_by_label_text(("Клиенты (компании, люди): ", "Просмотр"))
    app.settings_roles.get_custom_radio_by_label_text(("Автоматический учет трудозатрат"))
    app.settings_roles.get_custom_radio_by_label_text(("Автообновление заявок"))
    app.settings_roles.type_time_update("5")
    app.settings_roles.click_save_new_role_btn()
    app.base_page.check_notification_success("Выполнено успешно")
    app.base_page.refresh_page()
    app.settings_roles.check_value_in_list("Исполнительская_" + current_time)

    # Проверка изменения создание роли исполнителя
    app.settings_roles.type_search_filter("Исполнительская_" + current_time)
    app.settings_roles.type_name("Исполнительская_UPD" + current_time)
    app.settings_roles.choose_radio_by_label_text(("Заявки: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("Активы: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("База знаний: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("Сотрудники и группы: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("Клиенты (компании, люди): ", "Нет доступа"))
    app.settings_roles.get_custom_radio_by_label_text(("Автоматический учет трудозатрат"))
    app.settings_roles.get_custom_radio_by_label_text(("Автообновление заявок"))
    app.settings_roles.click_save_new_role_btn()
    app.base_page.check_notification_success("Выполнено успешно")
    app.base_page.refresh_page()
    app.settings_roles.check_value_in_list("Исполнительская_UPD" + current_time)

    # Удаление роли сотрудника и клиента
    app.wd.get(app.base_url + "settings/roles")
    app.settings_roles.remove_role([
        "Клиентская_" + current_time,
        "Исполнительская_UPD" + current_time])
    app.base_page.click_popup_yes_btn()
    app.base_page.check_notification_success("Данные успешно удалены")
    app.base_page.refresh_page()
    app.settings_roles.check_roles_was_removed([
        "Клиентская_" + current_time,
        "Исполнительская_UPD" + current_time])

    app.authorization.logout()
