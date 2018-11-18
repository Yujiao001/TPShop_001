import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class RegionPage(BaseAction):

    city_feature = By.ID,"com.tpshop.malls:id/tv_city"

    commit_button = By.XPATH,"//*[@text='确定']"

    region_msg=By.XPATH,"//*[@class='android.widget.TextView' and starts-with(@resource-id,'com.tpshop.malls:id/rb')]"

    @allure.step("选择地区页面-点击-省、市、区/县、镇/街道")
    def click_city(self):
        region_counts = len(self.find_elements(self.region_msg))
        for _ in range(region_counts):
            cities = self.find_elements(self.city_feature)
            random_city_index = random.randint(0,len(cities) - 1)
            cities[random_city_index].click()
            time.sleep(1)

    @allure.step("选择地区页面-点击-确定按钮")
    def click_commit(self):
        self.click(self.commit_button)

