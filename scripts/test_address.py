import time

from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_address(self):
        self.page.home.click_mine_button()

        if not self.page.mine.is_login():

            # 我的-登录/注册
            self.page.mine.click_login_and_sign_up()
            # 登录-输入用户名
            self.page.login.input_username("13800138006")
            # 登录-输入密码
            self.page.login.input_password("123456")
            # 登录-点击登录
            self.page.login.click_login_button()

        self.page.mine.click_address()
        # 新建地址
        self.page.address_list.click_add_address()
        # 添加联系人
        self.page.address.input_name("itcast")
        # 添加手机
        self.page.address.input_mobile("13888889999")
        self.page.address.input_address("南法信地铁站")
        self.page.address.click_region()
        self.page.region.click_city()
        self.page.region.click_commit()
        time.sleep(3)
        self.page.address.click_save_address()

        assert self.page.address.is_toast_exist("成功")


