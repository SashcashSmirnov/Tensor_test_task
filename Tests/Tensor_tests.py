import allure
from allure import step as Step
from Locators.Saby import SabyPageLocators
from Locators.Tensor import TensorPageLocators
from Pages.saby_page import SabyPage
from Pages.tensor_page import TensorPage
from seleniumbase import BaseCase
from Tests.conftest import open_saby_main_page


@allure.feature("Case 1. Проверка функциональности на сайте Сабу и Тензор")
@allure.severity(allure.severity_level.NORMAL)
class TensorUIVerificationTest(BaseCase):

    def test_links_and_ui_saby_tensor(self):
        with Step("Шаг 1: Открыть главную Сабу.ру"):
            open_saby_main_page(self)
            
        with Step("Шаг 2: Кликнуть на 'Контакты' в хедере"):
            self.hover_and_click(SabyPageLocators.CONTACTS_DROPDOWN_MENU, SabyPageLocators.CONTACTS)

        with Step("Шаг 3: Найти 'баннер Тензор' и кликнуть по нему"):
            self.click(TensorPageLocators.BANNER_TENSOR)

        with Step("Шаг 4: Найти блок 'Сила в людях'"):
            self.is_element_visible(TensorPageLocators.SILA_V_LUDIAH_BLOCK)

        with Step("Шаг 5: Кликнуть на кнопку 'Подробнее' в блоке 'Сила в людях'"):
            self.click_if_visible(TensorPageLocators.COOKIES_ALERT_CLOSE_BUTTON)
            self.click(TensorPageLocators.SILA_V_LUDIAH_DETAILED_BUTTON)

        with Step("Шаг 6: Проверить, что открылась страница 'tensor.ru/about'"):
            self.assert_title(TensorPageLocators.ABOUT_PAGE_TITLE)

        with Step("Шаг 7: Проверить, что 4 изображения в разделе 'Работаем' одного размера"):
            TensorPage.assert_images_equal_size(self, TensorPageLocators.IMAGES_WORKING_BLOCK)


@allure.feature("Case 2. Проверка функциональности на сайте Сабу.ру")
@allure.severity(allure.severity_level.NORMAL)
class SabyUIVerificationTest(BaseCase):
    
    def test_region_change_in_contacts(self):
        
        start_region = {"city": "Екатеринбург", "region": "Свердловская обл."}
        target_region = {"city": "Петропавловск-Камчатский", "region": "Камчатский край", "url": "kamchatskij-kraj"}


        with Step("Шаг 1: Открыть главную Сабу.ру"):
            open_saby_main_page(self)

        with Step("Шаг 2: Кликнуть на 'Контакты' в хедере"):
            self.hover_and_click(SabyPageLocators.CONTACTS_DROPDOWN_MENU, SabyPageLocators.CONTACTS, timeout=2)

        with Step("Шаг 3: Проверить, что указана Свердловская область"):
            self.assert_exact_text(start_region["region"], SabyPageLocators.REGION_LOCATION)

        with Step("Шаг 4: Проверить, что город Москва"):
            self.assert_exact_text(start_region["city"], SabyPageLocators.CITY_LOCATION)

        with Step("Шаг 5: Проверить, что есть партнеры"):
            SabyPage.count_number_of_partners_in_region(self)

        with Step("Шаг 6: Кликнуть на название региона"):
            self.click(SabyPageLocators.REGION_LOCATION)

        with Step("Шаг 7: Кликнуть на регион Камчатский край"):
            self.hover_and_click(SabyPageLocators.KAMCHATSKY_KRAY, SabyPageLocators.KAMCHATSKY_KRAY)

        with Step("Шаг 8: Проверить, что указан Камчатский край"):
            self.assert_exact_text(target_region["region"], SabyPageLocators.REGION_LOCATION)
            
        with Step("Шаг 9: Проверить, что город Петропавловск-Камчатский"):
            self.assert_exact_text(target_region["city"], SabyPageLocators.CITY_LOCATION)

        with Step("Шаг 10: Проверить, что есть партнеры"):
            SabyPage.count_number_of_partners_in_region(self)

        with Step("Шаг 11: Проверить, что тайтл Камчатский край"):
            self.assert_title(SabyPageLocators.KAMCHATSKY_KRAY_PAGE_TITLE)

        with Step("Шаг 12: Проверить, что в URL Камчатский край"):
            current_url = self.get_current_url()
            assert target_region["url"] in current_url, "URL не соответствует"


@allure.feature("Case 3. Проверка версии скачаного сетапа Сабу с сайта Сабу.ру с версией указанной на сайте")
@allure.severity(allure.severity_level.NORMAL)
class SabyDownloadVerificationVersionTest(BaseCase):

    def test_version_number_of_downloaded_setup(self):
        with Step("Шаг 1: Открыть главную Сабу.ру"):
            open_saby_main_page(self)

        with Step("Шаг 2: В Footer'e найти и перейти 'Скачать локальные версии'"):
            self.click(SabyPageLocators.DOWNLOAD_LOCAL)

        with Step("Шаг 3: Скачать ПО Сабу для Windows, в папку с тестом и сравнить версию скачанного файла с версией указанной на сайте"):
            SabyPage.verify_saby_downloaded_setup_version
