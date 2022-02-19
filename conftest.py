import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#добавляет параметр language для запуска теста
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language:\nar - to choose العربيّة\nca - to choose catal\ncs - to choose česky\nda - to choose dansk\nde - to choose Deutsc\nen-gb - to choose British English\nel - to choose Ελληνικά\nes - to choose español\nfi - to choose suomi\nfr - to choose français\nit - to choose italiano\nko - to choose 한국어\nnl - to choose Nederlands\npl - to choose polski\npt - to choose Português\npt-br - to choose Português Brasileiro\nro - to choose Română\nru - to choose Русский\nsk - to choose Slovensky\nuk - to choose Українська\nzh-hans - to choose 简体中文")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)    
    browser.implicitly_wait(5)
    print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()
