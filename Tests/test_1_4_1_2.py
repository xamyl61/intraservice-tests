# -*- coding: utf-8 -*-
import time


def test_1_4_1_2(app):
    current_time = "id_1.4.1.2"
    app.authorization.login(app.config["LOGIN"], app.config["PASSWORD"])

    # Создание роли сотрудника
    app.wd.get(app.base_url + "settings/roles")
    app.settings_roles.click_create_btn()
    app.settings_roles.type_name("РольИсп1_" + current_time)
    app.settings_roles.type_description("это_описание_роли_" + current_time)
    app.settings_roles.choose_role("Сотрудник")
    app.settings_roles.choose_radio_by_label_text(("Заявки: ", "Только свои"))
    app.settings_roles.choose_radio_by_label_text(("Активы: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("База знаний: ", "Нет доступа"))
    app.settings_roles.choose_radio_by_label_text(("Сотрудники и группы: ", "Просмотр"))
    app.settings_roles.choose_radio_by_label_text(("Клиенты (компании, люди): ", "Просмотр"))
    app.settings_roles.click_save_new_role_btn()
    app.base_page.check_notification_success("Выполнено успешно")
    app.base_page.refresh_page()
    app.settings_roles.check_value_in_list("РольИсп1_" + current_time)

    # Создание группы
    app.wd.get(app.base_url + "settings/usergroups")
    app.usergroups.click_create_btn()
    app.usergroups.type_name("Группа1_" + current_time)
    app.usergroups.click_save_btn()
    app.base_page.click_popup_yes_btn()
    app.base_page.check_notification_success("Выполнено успешно")

    # Создание сотрудника 1
    # time.sleep(2)
    app.wd.get(app.base_url + "settings/users/employees")
    app.settings_usersemployees.click_create_btn()
    app.settings_usersemployees.type_lastname("ФамилияСотр1" + current_time)
    app.settings_usersemployees.type_firstname("ИмяСотр1")
    app.settings_usersemployees.type_middlename("ОтчествоСотр1")
    app.settings_usersemployees.type_email("s1_" + current_time + "@gmail.com")
    app.settings_usersemployees.type_role("РольИсп1_" + current_time)
    app.settings_usersemployees.type_password("1")
    app.settings_usersemployees.type_password_confirmation("1")
    app.settings_usersemployees.type_group("Группа1_" + current_time)
    app.settings_usersemployees.click_save_btn()
    app.base_page.check_notification_success("Выполнено успешно")
    # app.base_page.refresh_page()

    # Создание сотрудника 2
    # time.sleep(2)
    app.settings_usersemployees.click_create_btn()
    app.settings_usersemployees.type_lastname("ФамилияСотр2" + current_time)
    app.settings_usersemployees.type_firstname("ИмяСотр2")
    app.settings_usersemployees.type_middlename("ОтчествоСотр2")
    app.settings_usersemployees.type_email("s2_" + current_time + "@gmail.com")
    app.settings_usersemployees.type_role("РольИсп1_" + current_time)
    app.settings_usersemployees.type_password("1")
    app.settings_usersemployees.type_password_confirmation("1")
    app.settings_usersemployees.type_group("Группа1_" + current_time)
    app.settings_usersemployees.click_save_btn()
    app.base_page.check_notification_success("Выполнено успешно")

    # Проверка что сотрудник создался
    app.base_page.refresh_page()
    app.settings_usersemployees.type_search("ФамилияСотр1" + current_time)
    app.settings_usersemployees.check_value_in_list("ФамилияСотр1" + current_time)

    # Изменение сотрудник 1
    app.settings_usersemployees.click_table_cell_name()
    app.settings_usersemployees.type_lastname("ФамилияСотр2" + current_time + "_изм")
    app.settings_usersemployees.type_firstname("ИмяСотр2" + "_изм")
    app.settings_usersemployees.type_middlename("ОтчествоСотр2" + "_изм")
    app.settings_usersemployees.type_email("s1_" + current_time + "changed" + "@gmail.com")
    app.settings_usersemployees.click_save_btn()
    app.base_page.check_notification_success("Выполнено успешно")
    app.base_page.refresh_page()

    # Проверка изменений сотрудника
    app.settings_usersemployees.click_clear_search()
    app.settings_usersemployees.type_search("ФамилияСотр2" + current_time + "_изм")
    app.settings_usersemployees.check_changed_fields("ФамилияСотр2" + current_time + "_изм",
                                                   "ИмяСотр2" + "_изм",
                                                   "ОтчествоСотр2" + "_изм",
                                                   "s1_" + current_time + "changed" + "@gmail.com")

    # Удаление сотрудников
    app.wd.get(app.base_url + "settings/users/employees")
    app.settings_usersemployees.click_clear_search()
    app.settings_usersemployees.remove_employee("ФамилияСотр2" + current_time + "_изм")
    app.base_page.check_notification_success("Удаление поставлено в очередь")
    app.base_page.check_notification_success("Успешно удалено")
    app.base_page.refresh_page()
    app.base_page.check_element_was_removed()

    app.settings_usersemployees.click_clear_search()
    app.settings_usersemployees.remove_employee("ФамилияСотр2" + current_time)
    app.base_page.check_notification_success("Удаление поставлено в очередь")
    app.base_page.check_notification_success("Успешно удалено")
    app.base_page.refresh_page()
    app.base_page.check_element_was_removed()

    # Удаление группы
    app.wd.get(app.base_url + "settings/usergroups")
    app.usergroups.remove_companies("Группа1_" + current_time)
    app.base_page.check_notification_success("Удаление поставлено в очередь")
    app.base_page.check_notification_success("Успешно удалено")
    app.base_page.refresh_page()
    app.base_page.check_element_was_removed()

    # Удаление роли сотрудника
    app.wd.get(app.base_url + "settings/roles")
    app.settings_roles.remove_role([
        "РольИсп1_" + current_time])
    app.base_page.click_popup_yes_btn()
    app.base_page.check_notification_success("Данные успешно удалены")
    app.base_page.refresh_page()
    app.settings_roles.check_roles_was_removed([
        "РольИсп1_" + current_time])

    app.authorization.logout()