import os
import sys

import pytest


def open_saby_main_page(self):
    self.open("https://saby.ru/")

def open_main_page_tensor(self):
    self.open("https://tensor.ru/")

def pytest_addoption(parser):
    """Добавляем кастомные опции командной строки"""
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Настройка seleniumbase перед запуском тестов"""
    if config.getoption("--headless"):
        # Устанавливаем переменные окружения для headless-режима
        os.environ["HEADLESS"] = "true"
        os.environ["DISPLAY"] = ":99"