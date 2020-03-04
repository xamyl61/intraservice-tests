import json
import time
import docker
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # for remote selenium

from Fixtures.application import Application

slenium_hub_port = 8899


@pytest.fixture(scope='session', autouse=1)
def run_browser_in_docker():
    client = docker.from_env()
    # docker run -d -p 4444:8899 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.12.0-cobalt
    container = client.containers.run(
        "selenium/standalone-chrome:latest",
        ports={4444: slenium_hub_port},
        volumes={'/dev/shm': {'bind': '/dev/shm', 'mode': 'rw'}},
        detach=True
    )

    time.sleep(10)  # TODO: make this smarter :)
    yield
    container.remove(force=True)


@pytest.fixture(scope='session',
                params=[
                    webdriver.Remote
                ],
                ids=[
                    'Remote_Chrome'
                ])
def driver(request):
    # # Create a new instance of a driver
    # driver = request.param(
    #     command_executor='http://localhost:{}/wd/hub'.format(slenium_hub_port),
    #     desired_capabilities=DesiredCapabilities.CHROME)
    # driver.implicitly_wait(30)
    # yield driver
    # driver.quit()

    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    capabilities = options.to_capabilities()

    # Create a new instance of a driver
    driver = request.param(
        command_executor='http://localhost:{}/wd/hub'.format(slenium_hub_port),
        desired_capabilities=capabilities)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()





# # for local run with browser
# @pytest.fixture(scope='session')
# def driver():
#     chrome_options = webdriver.ChromeOptions()
#     prefs = {"profile.default_content_setting_values.notifications": 2}
#     chrome_options.add_experimental_option("prefs", prefs)
#     driver = webdriver.Chrome(chrome_options=chrome_options,
#                               executable_path=r'/Users/alexanderonishchenko/Documents/intraservice-tests'
#                                               r'/chromedriver_mac64')
#     driver.implicitly_wait(30)
#     driver.maximize_window()
#     return driver


@pytest.fixture(scope="session")
def app(driver):
    global fixture
    with open('settings.json') as json_data_file:
        config = json.load(json_data_file)
    fixture = Application(driver, config)
    return fixture


def pytest_addoption(parser):
    parser.addoption(
        "--context_1.1", action="store", default="NoParam"
    )
    parser.addoption(
        "--context_1.2", action="store", default="NoParam"
    )
    parser.addoption(
        "--context_2.1", action="store", default="NoParam"
    )


@pytest.fixture(scope="module")
def context_1_1(request):
    return request.config.getoption("--context_1.1")


@pytest.fixture(scope="module")
def context_1_2(request):
    return request.config.getoption("--context_1.2")


@pytest.fixture(scope="session")
def context_2_1(request):
    return request.config.getoption("--context_2.1")


