import allure
import pytest


def open_saby_main_page(self):
    self.open("https://saby.ru/")

def open_main_page_tensor(self):
    self.open("https://tensor.ru/")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Добавление скриншота в allure при падении теста"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if hasattr(item.instance, 'driver') and item.instance.driver is not None:
            try:
                allure.attach(
                    item.instance.driver.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass