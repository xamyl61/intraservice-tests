# -*- coding: utf-8 -*-
import time
import config_variables


def test_1_4_1_1(app):
    current_time = "id_1.4.1.1"
    app.authorization.login(config_variables.LOGIN, config_variables.PASSWORD)
    # current_time = app.base_page.get_current_date_time()

    # Проверка создание роли клиента
    app.sidebar.click_sidebar_item("Настройки")
    app.settings.click_menu_by_text(["Справочники", "Роли"])
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

    # Создание роли сотрудника
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
    app.base_page.refresh_page()
    app.settings_roles.check_value_in_list("РольИсп1_" + current_time)

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

    # # Создание группы
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Группы"])
    # app.usergroups.click_create_btn()
    # app.usergroups.type_name("Группа1_" + current_time)
    # app.usergroups.click_save_btn()
    # app.base_page.click_popup_yes_btn()

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
        "РольКл1_" + current_time,
        "РольИсп1_" + current_time])
    app.base_page.click_popup_yes_btn()
    app.base_page.refresh_page()
    app.settings_roles.check_roles_was_removed([
        "РольКл1_" + current_time,
        "РольИсп1_" + current_time])



















    #
    # # Создатние сотрудника
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Люди(сотрудники)"])
    # app.settings_usersemployees.click_create_btn()
    # app.settings_usersemployees.type_lastname("Сотр_" + current_time)
    # app.settings_usersemployees.type_firstname("Константин")
    # app.settings_usersemployees.type_middlename("Алексеевич")
    # app.settings_usersemployees.type_email("is5_admin@intravision.ru")
    # app.settings_usersemployees.type_role(current_time + "_менеджер_Автотест")
    # app.settings_usersemployees.type_password("1")
    # app.settings_usersemployees.type_password_confirmation("1")
    # app.settings_usersemployees.click_save_btn()
    # app.base_page.refresh_page()
    #
    # # Создание нового сервиса
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Сервисы"])
    # app.settings_services.click_create_service()
    # app.settings_services.type_service_name("service_" + current_time)
    # app.settings_services.open_created_service("service_" + current_time)
    # app.settings_services.click_service_card_tab("Администраторы")
    # app.settings_services.type_search_name("Администраторов232 is5_admin_Семен Admin")
    # app.settings_services.click_save_btn()
    # app.settings_services.click_service_card_tab("Пользователи")
    # app.settings_services.click_radio_btn("Все клиенты")
    # app.settings_services.click_accept_btn()
    # app.settings_services.click_save_btn()
    # app.settings_services.click_service_card_tab("Типы заявок")
    # app.settings_services.type_search_name("Стандартный")
    # app.settings_services.click_checkbox("Доступно создание заявок")
    # app.settings_services.click_save_btn()
    #
    # # Создаем правило назначения бизнес-процесса
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Назначения бизнес-процесса"])
    # app.settings_rules_workflow.click_new_rule()
    # time.sleep(2)
    # app.settings_rules_workflow.type_service_name("service_" + current_time)
    # app.settings_rules_workflow.choose_business_process_item("Простой_HelpDesk_не_стирать")
    # app.settings_rules_workflow.click_save_btn()
    # app.settings_services.click_accept_btn()
    # app.base_page.refresh_page()
    # app.settings_rules_workflow.type_search_filter("service_" + current_time)
    # app.settings_rules_workflow.check_search_results("service_" + current_time)
    #
    # # Назначение исполнителей - добавить для созданного ранее сервиса и созданного ранее сотрудника настройку
    # app.sidebar.click_sidebar_item("Настройки")
    # app.business_process.type_search_filter("Простой_HelpDesk_не_стирать")
    # app.business_process.click_search_text("Простой_HelpDesk_не_стирать")
    # app.base_page.click_tab("Назначение исполнителей")
    # time.sleep(6)
    # app.settings_business_process_card.click_assign_executor_group_btn()
    # app.settings_business_process_card.choose_assignment("Сотр_" + current_time + " Константин Алексеевич")
    # app.settings_business_process_card.choose_business_process("service_" + current_time)
    # app.settings_business_process_card.click_save_btn("Сотр_" + current_time + " Константин Алексеевич")
    # app.base_page.refresh_page()
    # app.settings_business_process_card.type_search_filter("service_" + current_time)
    # time.sleep(4)
    # app.settings_business_process_card.check_search_results((
    #     "service_" + current_time, "Сотр_" + current_time + " Константин Алексеевич"))

    # # Зайти под новым пользователем в клиентский портал и создать заявку в новом сервисе
    # app.authorization.logout()
    # app.base_page.refresh_page()
    # app.authorization.login("k1_" + current_time + "@gmail.com", "1")
    # app.dashboard.click_create_task()
    # app.dashboard.open_created_service("service_" + current_time)
    # app.dashboard.check_cursor_in_name_field()
    # app.dashboard.type_task_name("Новая_заявкаАвтотеста " + current_time)
    # app.dashboard.click_save_btn()
    # time.sleep(4)
    # app.dashboard.check_created_task("Новая_заявкаАвтотеста " + current_time)
    # time.sleep(10)
    # app.dashboard.click_logout_btn()
    # #
    # # Зайти под исполнителем в данную заявку и добавить комментарий.
    # app.authorization.login("d1_" + current_time + "test@gmail.com", "1")
    # app.client_portal.check_url()
    # app.client_portal.click_reset_filter_btn()
    # app.client_portal.check_executor_in_results("Новая_заявкаАвтотеста " + current_time)
    # app.client_portal.click_first_row_name()
    # app.client_portal.type_text_editor("Мы начали работать!")
    # app.client_portal.click_save_editor_btn()
    # app.base_page.refresh_page()
    # app.client_portal.check_comment_added("Мы начали работать!")
    # app.client_portal.click_logout_btn()
    #
    # # Удаление заявки
    # app.authorization.login('is5_admin@intravision.ru', '111111')
    # app.tasks.choose_task_in_table("Новая_заявкаАвтотеста " + current_time)
    # app.tasks.click_action_btn_remove()
    # app.base_page.refresh_page()
    # app.tasks.check_name_was_removed("Новая_заявкаАвтотеста " + current_time)
    #
    # # Удаление исполнителя в карточке бизнес-процесса
    # app.sidebar.click_sidebar_item("Настройки")
    # app.business_process.type_search_filter("Простой_HelpDesk_не_стирать")
    # app.business_process.click_search_text("Простой_HelpDesk_не_стирать")
    # app.base_page.click_tab("Назначение исполнителей")
    # time.sleep(6)
    # app.business_process.choose_executor_in_table("service_" + current_time)
    # app.business_process.click_remove_executors_btn()
    # app.base_page.click_popup_yes_btn()
    # app.business_process.check_executor_was_removed("service_" + current_time)
    #
    # # Удалить правило назначения бизнес-процесса для сервиса
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Назначения бизнес-процесса"])
    # app.settings_rules_workflow.type_search_filter("service_" + current_time)
    # app.settings_rules_workflow.choose_rule_in_table("service_" + current_time)
    # app.settings_rules_workflow.click_remove_rule_btn()
    # app.base_page.click_popup_yes_btn()
    # time.sleep(6)
    # app.base_page.refresh_page()
    # app.settings_rules_workflow.check_ruele_was_removed()
    #
    # # Удаление сервиса
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Сервисы"])
    # app.settings_services.remove_service_from_tree("service_" + current_time)
    # app.base_page.click_remove_modal_yes_btn()
    # app.base_page.click_popup_yes_btn()
    # app.settings_services.check_service_was_removed("service_" + current_time)
    #
    # # Удаление сотрудника
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Люди(сотрудники)"])
    # app.settings_usersemployees.type_search("d1_" + current_time + "test@gmail.com")
    # app.settings_usersemployees.choose_rule_in_table("d1_" + current_time + "test@gmail.com")
    # app.settings_usersemployees.click_remove_btn()
    # app.base_page.click_popup_yes_btn()
    # app.base_page.refresh_page()
    # app.settings_usersemployees.check_employee_was_removed()
    #
    # # Удаление клиента
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Люди(клиенты)"])
    # app.settings_usersclients.remove_client("k1_" + current_time + "@gmail.com")
    # app.base_page.refresh_page()
    # app.base_page.check_element_was_removed()
    #
    # # Удаление компании
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Компании"])
    # app.settings_clientcompanies.remove_companies(current_time + "_Интересная_Компания")
    # app.base_page.refresh_page()
    # app.base_page.check_element_was_removed()
    #
    # # Удаление роли сотрудника
    # app.sidebar.click_sidebar_item("Настройки")
    # app.settings.click_menu_by_text(["Справочники", "Роли"])
    # app.settings_roles.remove_role([
    #     current_time + "_менеджер_Автотест",
    #     current_time + "_клиент_Автотест"])
    # app.base_page.click_popup_yes_btn()
    # app.base_page.refresh_page()
    # app.settings_roles.check_roles_was_removed([
    #     current_time + "_менеджер_Автотест",
    #     current_time + "_клиент_Автотест"])
    #
    #
    # time.sleep(3)