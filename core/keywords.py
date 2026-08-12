import logging
import time


import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def open(self,step):
        """打开网址"""
        with allure.step(f'第{step["step_num"]}步：{step["step_name"]}'):
            logging.info(f'第{step["step_num"]}步：{step["step_name"]}')
            self.driver.get(step["data"])

    def click(self, step):
        """点击"""
        with allure.step(f'第{step["step_num"]}步：{step["step_name"]}'):
            logging.info(f'第{step["step_num"]}步：{step["step_name"]}')
            #self.driver.find_element(step["by"],step["value"]).click()
            self.driver.find(step).click()

    def input(self,step):
        """输入文本"""
        with allure.step(f'第{step["step_num"]}步：{step["step_name"]}'):
            logging.info(f'第{step["step_num"]}步：{step["step_name"]}')
            self.driver.find(step).send_keys(step["data"])
            #self.driver.find_element(step["by"],step["value"]).send_keys(step["data"])

    def clear(self, step):
        """清空文本"""
        with allure.step(f'第{step["step_num"]}步：{step["step_name"]}'):
            logging.info(f'第{step["step_num"]}步：{step["step_name"]}')
            #self.driver.find_element(step["by"],step["value"]).clear()
            self.driver.find(step).clear()

    def wait(self,step):
        """等待"""
        with allure.step(f'第{step["step_num"]}步：{step["step_name"]}'):
            logging.info(f'第{step["step_num"]}步：{step["step_name"]}')
            time.sleep(step["data"])

