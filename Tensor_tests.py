import pytest
import allure
import re
from seleniumbase import BaseCase
from utils.checks import assert_images_equal_size, count_number_of_partners_in_region, verify_saby_download
from utils.locators import SabyPage, TensorPage
from allure import step as Step

@pytest.mark.smoke
@allure.feature("Case 1. Проверка функциональности на сайте Сабу и Тензор")
@allure.severity(allure.severity_level.NORMAL)
class TensorUIVerificationTest(BaseCase):

    def test_links_and_ui_sbis_tensor(self):
        with Step("Шаг 1: Открыть главную Сабу.ру"):
            self.open(SabyPage.SABY_MAIN_PAGE)

        with Step("Шаг 2: Кликнуть на 'Контакты' в хедере"):
            self.hover_and_click(SabyPage.CONTACTS_DROPDOWN_MENU, SabyPage.CONTACTS)

        with Step("Шаг 3: Найти 'баннер Тензор' и кликнуть по нему"):
            self.click(TensorPage.BANNER_TENSOR)

        with Step("Шаг 4: Найти блок 'Сила в людях'"):
            self.assert_text(TensorPage.SILA_V_LUDIAH_BLOCK)

        with Step("Шаг 5: Кликнуть на кнопку 'Подробнее' в блоке 'Сила в людях'"):
            self.click_if_visible(TensorPage.COOKIES_ALERT_CLOSE_BUTTON, timeout=2)
            self.click(TensorPage.SILA_V_LUDIAH_DETAILED_BUTTON)

        with Step("Шаг 6: Проверить, что открылась страница 'tensor.ru/about'"):
            self.assert_title(TensorPage.ABOUT_PAGE_TITLE)

        with Step("Шаг 7: Проверить, что 4 изображения в разделе 'Работаем' одного размера"):
            assert_images_equal_size(self, TensorPage.IMAGES_WORKING_BLOCK)


@pytest.mark.smoke
@allure.feature("Case 2. Проверка функциональности на сайте Сабу.ру")
@allure.severity(allure.severity_level.NORMAL)
class SabyUIVerificationTest(BaseCase):
    def test_region_change_in_contacts(self):
        
        start_region = {"city": "Екатеринбург", "region": "Свердловская обл."}
        target_region = {"city": "Петропавловск-Камчатский", "region": "Камчатский край"}

        with Step("Шаг 1: Открыть главную Сабу.ру"):
            self.open(SabyPage.SABY_MAIN_PAGE)

        with Step("Шаг 2: Кликнуть на 'Контакты' в хедере"):
            self.hover_and_click(SabyPage.CONTACTS_DROPDOWN_MENU, SabyPage.CONTACTS)

        with Step("Шаг 3: Проверить, что указана Свердловская область"):
            self.assert_exact_text(start_region["region"], SabyPage.REGION_LOCATION)
            
        with Step("Шаг 4: Проверить, что город Екатеринбург"):
            self.assert_exact_text(start_region["city"], SabyPage.CITY_LOCATION)

        with Step("Шаг 5: Проверить, что есть партнеры"):
            count_number_of_partners_in_region(self)

        with Step("Шаг 6: Кликнуть на название региона"):
            self.click(SabyPage.REGION_LOCATION)

        with Step("Шаг 7: Кликнуть на регион Камчатский край"):
            self.hover_and_click(SabyPage.KAMCHATSKY_KRAY, SabyPage.KAMCHATSKY_KRAY)

        with Step("Шаг 8: Проверить, что указан Камчатский край"):
            self.assert_exact_text(target_region["region"], SabyPage.REGION_LOCATION)
            
        with Step("Шаг 9: Проверить, что город Петропавловск-Камчатский"):
            self.assert_exact_text(target_region["city"], SabyPage.CITY_LOCATION)

        with Step("Шаг 10: Проверить, что есть партнеры"):
            count_number_of_partners_in_region(self)

        with Step("Шаг 11: Проверить, что тайтл Камчатский край"):
            self.assert_title(SabyPage.KAMCHATSKY_KRAY_PAGE_TITLE)

        with Step("Шаг 12: Проверить, что в URL Камчатский край"):
            current_url = self.get_current_url()
            assert re.search(r"kamchatskij-kraj", current_url), "URL не соответствует"


@pytest.mark.smoke
@allure.feature("Case 3. Проверка версии скачаного сетапа Сабу с сайта Сабу.ру с версией указанной на сайте")
@allure.severity(allure.severity_level.NORMAL)
class SabyDownloadVerificationVersionTest(BaseCase):

    def test_version_number_of_downloaded_setup(self):
        with Step("Шаг 1: Открыть главную Сабу.ру"):
            self.open(SabyPage.SABY_MAIN_PAGE)

        with Step("Шаг 2: В Footer'e найти и перейти 'Скачать локальные версии'"):
            self.click(SabyPage.DOWNLOAD_LOCAL)

        with Step("Шаг 3: Скачать ПО Сабу для Windows, в папку с тестом и сравнить версию скачанного файла с версией указанной на сайте"):
            verify_saby_download(self)
