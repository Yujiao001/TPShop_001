from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_username(self, text):
        self.input(self.username, text)

    def input_password(self, text):
        self.input(self.password, text)

    def click_login_button(self):
        self.click(self.login_button)

    def is_toast_exist(self, text):
        toast_feature = By.XPATH, "//*[contain(@text,'%s')]" % text
        try:
            self.find_element(toast_feature, timeout=5)
            return True
        except Exception as e:
            return False