import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.fixture(scope="class")
def setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


def pytest_html_report_title(report):
    report.title = 'DEPT Exercise Report'

