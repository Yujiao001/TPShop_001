import time

import pytest

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        print("test_login")

    @pytest.mark.parametrize("args",analyze_with_file("data_login_msg", "test_login1"))
    def test_login1(self, args):
        time.sleep(5)
        # 首页-我的
        self.page.home.click_mine_button()
        # 我的 登录/注册
        self.page.mine.click_login_and_sign_up()

        # 输入用户名
        username = args["username"]
        self.page.login.input_username(username)
        # 输入密码
        password = args["password"]
        self.page.login.input_password(password)
        # 点击登录
        toast_msg = args["toast_msg"]
        self.page.login.click_login_button()
        print(toast_msg)
        assert self.page.login.is_toast_exist(toast_msg)
