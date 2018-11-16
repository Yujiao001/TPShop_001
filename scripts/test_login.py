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

    @pytest.mark.parametrize("args",analyze_with_file("login_data", "test_login"))
    def test_login(self, args):
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
        assert self.page.login.is_toast_exist(toast_msg)

    @pytest.mark.parametrize("args",analyze_with_file("login_data", "test_login_miss_part"))
    def test_login_miss_part(self,args):
        # 准备数据
        username = args["username"]
        password = args["password"]

        # 首页-我的
        self.page.home.click_mine_button()
        # 我的 登录/注册
        self.page.mine.click_login_and_sign_up()
        # 登录的页面输入用户名和密码
        # 方式一：数据设计时设计成空
        self.page.login.input_username(args["username"])
        self.page.login.input_password(args["password"])

        # 断言，如果按钮不可用则通过，如果按钮可用则不通过
        assert not self.page.login.is_login_button_enabled()

        # 方法二：如果数据设计的时候，没有不输入的key,使用下面的方法
        # if "username" in args:
        #     self.page.login.input_username(args["username"])
        #
        # if "password" in args:
        #     self.page.login.input_password(args["password"])

