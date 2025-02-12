from time import sleep

from selene import browser
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')
    s(".mr-2.color-fg-muted").click()
    s(".FormControl-input").send_keys('eroshenkoam/allure-example')
    s(".FormControl-input").submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s("#issues-repo-tab-count").click()

    s(by.text('95')).should(be.visible)

    sleep(3)