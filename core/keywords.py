import logging
import time


import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.keywords_utils import kw_step


class Keywords:

    def __init__(self,driver):
        self.driver=driver
    def find(self,step):
        wait= WebDriverWait(self.driver,10)
        locator=step["by"],step["value"]

        #如果索引为None，则定位单个单元，反之定位一组元素
        if step["index"] is None:
            return wait.until(EC.presence_of_element_located(locator))
        else:
            return wait.until(EC.presence_of_element_located(locator))[step["index"]]

    @kw_step
    def open(self,step):
        """打开网址"""
        self.driver.get(step["data"])

    @kw_step
    def click(self, step):
        """点击"""
        #self.driver.find_element(step["by"],step["value"]).click()
        self.find(step).click()

    @kw_step
    def input(self,step):
        """输入文本"""
        self.find(step).send_keys(step["data"])
        #self.driver.find_element(step["by"],step["value"]).send_keys(step["data"])

    @kw_step
    def clear(self, step):
        """清空文本"""
        #self.driver.find_element(step["by"],step["value"]).clear()
        self.find(step).clear()

    @kw_step
    def wait(self,step):
        """等待"""
        time.sleep(step["data"])

