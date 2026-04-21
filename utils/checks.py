import os
import re
import requests
import pefile
from utils.locators import SabyPage


def assert_images_equal_size(test, selector, count=4):
    imgs = test.find_elements(selector)[:count]
    sizes = [(test.execute_script("return arguments[0].width", img),
              test.execute_script("return arguments[0].height", img)) for img in imgs]
    assert all(s == sizes[0] for s in sizes), f"Размеры: {sizes}"
    print(f"✅ {count} картинок: {sizes[0][0]}x{sizes[0][1]}")


def count_number_of_partners_in_region(self):
    partners = self.find_elements(SabyPage.PARTNERS_LIST)
    partners_count = len(partners)
    print(f"Найдено партнёров: {partners_count}")
    self.assert_true(partners_count >= 1,
                     f"Количество партнёров {partners_count}, ожидалось 1 или больше")
    print(f"✅ Количество партнёров: {partners_count} (минимум 1)")


def get_version_from_site(test_case):
    """Получение версии с сайта"""
    text = test_case.get_text('.sbis_ru-DownloadNew__version')
    match = re.search(r'(\d+\.\d+\.\d+)', text)
    assert match, f"Версия не найдена в тексте: {text}"
    return match.group(1)


def download_file(test_case, file_name="saby-setup.exe"):

    BASE_DOWNLOAD_DIR = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), "downloaded_files")
    file_link = test_case.get_attribute('a[href*="saby-setup.exe"]', "href")

    os.makedirs(BASE_DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(BASE_DOWNLOAD_DIR, file_name)

    response = requests.get(file_link, stream=True)
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    return file_path


def check_file_version(file_path, expected_version):
    """Проверка версии файла"""
    if not os.path.exists(file_path):
        return False, f"Файл не найден: {file_path}"

    pe = pefile.PE(file_path)
    for fileinfo in pe.FileInfo:
        for entry in fileinfo:
            if hasattr(entry, 'StringTable'):
                for st in entry.StringTable:
                    if b'FileVersion' in st.entries:
                        version = st.entries[b'FileVersion'].decode('utf-8')
                        version = version.rstrip('.0')
                        return version == expected_version, version

    return False, "Версия не найдена"


def verify_saby_download(test_case):
    """Полная проверка скачивания и версии"""
    expected_version = get_version_from_site(test_case)
    file_path = download_file(test_case)
    result, file_version = check_file_version(file_path, expected_version)
    assert result, f"Версия {file_version} не совпадает с {expected_version}"
    print(f"✅ Версия {file_version} совпадает!")
