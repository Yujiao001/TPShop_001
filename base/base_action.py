from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def text(self,feature):
        return self.find_element(feature).text

    def last_element_text(self, feature):
        return self.find_elements(feature)[-1].text

    def is_toast_exist(self, text):
        toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % text
        try:
            self.find_element(toast_feature, timeout=5, poll=0.5)
            # self.find_element((By.XPATH,"//*[contains(@text,'%s')]" % text),timeout=5)
            return True
        except Exception as e:
            return False


