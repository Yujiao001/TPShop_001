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

    # 查看某一个元素是否可用
    def is_feature_enabled(self, feature):
        return self.find_element(feature).is_enabled()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

    def last_element_text(self, feature):
        return self.find_elements(feature)[-1].text

    # def is_toast_exist(self, text):
    #     toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % text
    #     try:
    #         self.find_element(toast_feature, timeout=5, poll=0.5)
    #         # self.find_element((By.XPATH,"//*[contains(@text,'%s')]" % text),timeout=5)
    #         return True
    #     except Exception as e:
    #         return False

    def is_toast_exist(self, text, is_contains = True):
        toast_feature_value = "//*[contains(@text,'%s')]" % text
        if not is_contains:
            toast_feature_value = "//*[@text='%s']" % text
        try:
            self.find_element((By.XPATH, toast_feature_value), timeout=5, poll=0.5)
            return True
        except Exception as e:
            return False

    """
    滑动
    """
    def scroll_page_one_time(self, direction="up"):
        """
        调用一次滑动一屏
        :param direction: 方向 默认为从下往上
            "up":从下往上 "down":从上往下 "left":从右往左 "right":从左往右
        :return:
        """

        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y =screen_height * 0.5
        top_x = center_x
        top_y = screen_height * 0.25
        buttom_x = center_x
        buttom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        left_y = center_y
        right_x = screen_width * 0.75
        right_y = center_y

        if direction == "up":
            self.driver.swipe(buttom_x, buttom_y, top_x, top_y)
        elif direction =="bottom":
            self.driver.swipe(top_x, top_y, buttom_x, buttom_y)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        else:
            raise Exception("请输入正确的参数，up/down/left/right")


        # start_x = screen_width * 0.5
        # start_y = screen_height * 0.75
        # end_x = start_x
        # end_y = start_y * 0.25
        # self.driver.swip(start_x, start_y, end_x, end_y)

    """
    一边滑动一边找
    """
    def is_feature_exist_scroll_page(self, feature, direction="up"):
        old_source = ""
        while True:
            try:
                old_source = self.driver.page_source
                self.find_element(feature)
                return True
            except Exception:
                self.scroll_page_one_time(direction)
                if old_source == self.driver.page_source:
                    return False

