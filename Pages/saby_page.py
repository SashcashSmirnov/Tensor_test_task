import os
import re
import requests
import pefile 
from Locators.Saby import SabyPage

def open_sbis_main_page(self):
        self.open("https://sbis.ru/")


def count_number_of_partners_in_region(self):
        partners = self.find_elements(SabyPage.PARTNERS_LIST)
        partners_count = len(partners)
        print(f"Найдено партнёров: {partners_count}")
        self.assert_true(partners_count >= 1, f"Количество партнёров {partners_count}, ожидалось 1 или больше")
        print(f"✅ Количество партнёров: {partners_count} (минимум 1)")


def get_version_from_site(test_case):
        text = test_case.get_text(SabyPage.SABY_DOWNLOAD_VERSION)   
        match = re.search(r'(\d+\.\d+\.\d+)', text)
        assert match, f"Версия не найдена в тексте: {text}"
        return match.group(1)


def download_file(test_case, file_name="saby-setup.exe"):
        BASE_DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "downloaded_files")
        file_link = test_case.get_attribute(SabyPage.SABY_SETUP_DOWNLOAD, "href")   
        os.makedirs(BASE_DOWNLOAD_DIR, exist_ok=True)
        file_path = os.path.join(BASE_DOWNLOAD_DIR, file_name)
        response = requests.get(file_link, stream=True)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return file_path


def check_file_version(file_path, expected_version):
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


def verify_saby_downloaded_setup_version(test_case):
        expected_version = get_version_from_site(test_case)
        file_path = download_file(test_case)
        result, file_version = check_file_version(file_path, expected_version)
        assert result, f"Версия {file_version} не совпадает с {expected_version}"
        print(f"✅ Версия {file_version} совпадает!")