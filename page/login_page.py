from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class LoginPage(BaseAction):

    username = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    show_password_button = By.ID,'com.tpshop.malls:id/img_view_pwd'

    @allure.step("登录页面-输入-用户名")
    def input_username(self, text):
        allure.attach("用户名",text)
        self.input(self.username, text)

    @allure.step("登录页面-输入-密码")
    def input_password(self, text):
        allure.attach("密码", text)
        self.input(self.password, text)

    @allure.step("登录页面-点击-登录按钮")
    def click_login_button(self):
        self.click(self.login_button)

    @allure.step("登录页面-点击-显示密码")
    def click_show_password(self):
        self.click(self.show_password_button)

        # 会把截图保存到项目中并上传
        # self.driver.get_screenshot_as_file("xx.png")
        # with open("xx.png","rb") as f:
        #     allure.attach("截图", f.read(), allure.attach_type.PNG)

        # 直接上传
        allure.attach("截图",self.driver.get_screenshot_as_png,allure.attach_type.PNG)


    # 判断按钮是否可见
    def is_login_button_enabled(self):
        # 写到base中后用下面的直接使用就可以
        return self.is_feature_enabled(self.login_button)
        # 方式一（提倡，简单）：
        # return self.find_element(self.login_button).is_enabled()
        # 方式二：
        # if self.find_element(self.login_button).get_attribute("enabled") == "true":
        #     return True
        # return False

    def get_password_text(self):
        return self.get_text(self.password)
