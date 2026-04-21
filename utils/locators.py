class SabyPage:
    SABY_MAIN_PAGE = "https://sbis.ru/"
    CONTACTS = 'a[href="/contacts"]'
    CONTACTS_DROPDOWN_MENU = '.sbisru-MenuPopupTemplate__title.ws-flexbox.ws-align-items-start.pv-8.controls-PopupPreviewer'
    REGION_LOCATION = '.sbis_ru-Region-Chooser__text.sbis_ru-link'
    CITY_LOCATION = ".sbisru-Contacts-List__city.sbisru-text--standart.sbisru-Contacts__text--500"
    PARTNERS_LIST = ".sbisru-Contacts-List__item.sbisru-text--standart.sbisru-Contacts__text--500"
    KAMCHATSKY_KRAY = '.sbis_ru-link:contains("Камчатский край")'
    KAMCHATSKY_KRAY_PAGE_TITLE = "Saby Контакты — Камчатский край"
    KAMCHATSKY_KRAY_URL = "https://saby.ru/contacts/41-kamchatskij-kraj"
    DOWNLOAD_LOCAL = "a[href='/download']"
    SABY_DOWNLOAD_VERSION = ".sbis_ru-DownloadNew__version"


class TensorPage:
    TENSOR_MAIN_PAGE = "https://tensor.ru/"
    BANNER_TENSOR = 'a[href="https://tensor.ru/"]'
    SILA_V_LUDIAH_BLOCK = "Сила в людях"
    SILA_V_LUDIAH_DETAILED_BUTTON = '//*[contains(text(), "Сила в людях")]/ancestor::div[contains(@class, "tensor_ru-Index__card")]//a[text()="Подробнее"]'
    ABOUT_PAGE_TITLE = 'О компании | Тензор — IT-компания'
    IMAGES_WORKING_BLOCK = '.tensor_ru-About__block3-image'
    COOKIES_ALERT_CLOSE_BUTTON = '.sbis_ru-CookieAgreement__close'
