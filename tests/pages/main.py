# coding=utf-8

from base import *
from tests.elements.main import *


class MainPage(BasePage):
    url = 'http://ftest.tech-mail.ru/feed/'

    def wait_username(self):
        UserDropdown(self.driver).get()

    def get_username(self):
        self.navigate()
        return UserDropdown(self.driver).get().text
