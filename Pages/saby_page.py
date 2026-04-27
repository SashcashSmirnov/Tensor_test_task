import os
import re

import pefile
import requests
from Locators.Saby import SabyPageLocators


class SabyPage():
        
        def count_number_of_partners_in_region(self):
                partners = self.find_elements(SabyPageLocators.PARTNERS_LIST)
                partners_count = len(partners)
                self.assert_true(partners_count >= 1, f"Количество партнёров {partners_count}, ожидалось 1 или больше")
                
        def get_version_from_site(test_case):
                text = test_case.get_text(SabyPageLocators.SABY_DOWNLOAD_VERSION)   
                match = re.search(r'(\d+\.\d+\.\d+)', text)
                assert match, f"Версия не найдена в тексте: {text}"
                return match.group(1)

        def download_file(test_case, file_name="saby-setup.exe"):
                BASE_DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "downloaded_files")
                file_link = test_case.get_attribute(SabyPageLocators.SABY_SETUP_DOWNLOAD, "href")   
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

        def verify_saby_downloaded_setup_version(self, test_case):
                expected_version = self.get_version_from_site(test_case)
                file_path = self.download_file(test_case)
                result, file_version = self.check_file_version(file_path, expected_version)
                assert result, f"Версия {file_version} не совпадает с {expected_version}"