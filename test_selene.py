from time import sleep

import allure
from selene import browser
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


def test_github():

    with allure.step('open main page'):
        browser.open('https://github.com/')

    with allure.step('searching repo'):
        s(".mr-2.color-fg-muted").click()
        s(".FormControl-input").send_keys('eroshenkoam/allure-example')
        s(".FormControl-input").submit()

    with allure.step('click on repo_name'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('click on issues icon'):
        s("#issues-repo-tab-count").click()

    with allure.step('check - find text'):
        s(by.text('Тестируем тест')).should(be.visible)