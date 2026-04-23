from seleniumbase import BaseCase

class TensorPage(BaseCase):
    
    BANNER_TENSOR = 'a[href="https://tensor.ru/"]'
    SILA_V_LUDIAH_BLOCK = "Сила в людях"
    SILA_V_LUDIAH_DETAILED_BUTTON = '//*[contains(text(), "Сила в людях")]/ancestor::div[contains(@class, "tensor_ru-Index__card")]//a[text()="Подробнее"]'
    ABOUT_PAGE_TITLE = 'О компании | Тензор — IT-компания'
    IMAGES_WORKING_BLOCK = '.tensor_ru-About__block3-image'
    COOKIES_ALERT_CLOSE_BUTTON = '.sbis_ru-CookieAgreement__close'
