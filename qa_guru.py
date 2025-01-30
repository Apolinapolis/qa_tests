import os.path
import time

import requests
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from script_open import TMP_DIR


# options = webdriver.ChromeOptions()
# prefs = {
#     "download.default_directory": "/users/dm.yudin/Develop/qa_tests/tmp",
#     "download.prompt_for_download": False
# }
#
# options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# browser.config.driver = driver
# browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
# dl_url = browser.element("[data-testid='raw-button']").get(query.attribute('href'))
# content = requests.get(url=dl_url).content
#
# with open('tmp/test1.rst', "wb") as file:
#     file.write(content)

def test_read_file():
    with open(os.path.join(TMP_DIR, 'README.rst'), 'r') as file:
        file_content = file.read()
        assert "For full documentation, including installation" in file_content