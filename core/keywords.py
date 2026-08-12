import logging
import time


import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.keywords_utils import kw_step


class Keywords:

    def __init__(self,driver):
        self.driver=driver
    def find(self,step):
        wait= WebDriverWait(self.driver,10)
        locator=step["by"],step["value"]

        try:
            # 如果索引为None，则定位单个单元，反之定位一组元素
            if step["index"] is None:
                return wait.until(EC.presence_of_element_located(locator))
            else:
                return wait.until(EC.presence_of_element_located(locator))[step["index"]]
        except TimeoutException:
            logging.error(f"❌️元素定位失败，元素定位信息为{locator}")



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


    #断言关键字
    @kw_step
    def assert_url(self,step):
        """url断言"""
        expected_url=step["data"]
        actual_url=self.driver.current_url

        assert expected_url in actual_url,f"❌️当前url:{actual_url} 不包含 预期url:{expected_url}"
        logging.info(f"✅️当前url:{actual_url} 包含 预期url:{expected_url}")

        # #捕获异常
        # try:
        #     assert expected_url in actual_url
        #     logging.info(f"✅️当前url:{actual_url} 包含 预期url:{expected_url}")
        # except AssertionError:
        #     logging.error(f"❌️当前url:{actual_url} 不包含 预期url:{expected_url}")


    @kw_step
    def assert_title(self,step):
        """title 断言"""
        expected_title=step["data"]
        actual_title=self.driver.title
        assert expected_title in actual_title, f"❌️当前title:{actual_title} 不包含 预期title:{expected_title}"
        logging.info(f"✅️当前title:{actual_title} 包含 预期title:{expected_title}")

    @kw_step
    def assert_text(self,step):
        """text断言"""
        expected_text=step["data"]
        actual_text=self.find(step).text
        assert expected_text in actual_text, f"❌️当前text:{actual_text} 不包含 预期text:{expected_text}"
        logging.info(f"✅️当前text:{actual_text} 包含 预期text:{expected_text}")

    @kw_step
    def assert_alert_text(self,step):
        expected_text = step["data"]
        actual_text = self.find(step).text
        assert expected_text in actual_text, f"❌️当前text:{actual_text} 不包含 预期text:{expected_text}"
        logging.info(f"✅️当前text:{actual_text} 包含 预期text:{expected_text}")

    @kw_step
    def assert_element_exist(self,step):
        """元素存在断言"""
        element=self.find(step)
        assert element,f"❌️元素不存在{element}"
        logging.info(f"✅️元素存在:{element}")
