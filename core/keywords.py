import logging
import os
import time


import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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


    @kw_step
    def shot(self,step):
        """截图"""
        #获取时间
        now_time=time.strftime("%Y-%m-%d %H:%M:%S")

        png=self.driver.get_screenshot_as_png()
        allure.attach(
            png,
            f'第{step["step_num"]}步_{now_time}.png',
            attachment_type=allure.attachment_type.PNG)

    #浏览器基本操作:刷新，前进，后退，根据句柄切换到初始窗口
    @kw_step
    def refresh(self,step):
        """刷新"""
        self.driver.refresh()

    @kw_step
    def forward(self,step):
        """前进"""
        self.driver.forward()

    @kw_step
    def back(self, step):
        """后退"""
        self.driver.back()

    @kw_step
    def switch_to_window(self, step):
        """切换窗口（根据句柄索引）"""
        handles=self.driver.window_handles
        self.driver.switch_to_window(handles[step["data"]])

    #下拉框操作:通过文本选择，通过值选择
    @kw_step
    def select_by_text(self, step):
        """通过文本选择"""
        select=Select(self.find(step))
        select.select_by_visible_text(step["data"])

    @kw_step
    def select_by_value(self, step):
        """通过值选择"""
        select = Select(self.find(step))
        select.select_by_value(step["data"])

    #弹出框操作：接受，拒绝
    @kw_step
    def accept_alert(self, step):
        """接受"""
        self.driver.switch_to_alert.accept()

    @kw_step
    def dismiss_alert(self, step):
        """拒绝"""
        self.driver.switch_to_alert.dismiss()

    # 滚动条操作：滚动和js执行操作
    @kw_step
    def scroll_to(self, step):
        """
        滚动到某个绝对坐标位置
        step["data"]数据要写成字典{'x':100,'y':100}形式
        """
        position=eval(step["data"])
        js=f"window.scrollTo({position.dict['x']},{position.dict['y']})"
        self.driver.execute_script(js)

    @kw_step
    def execute_js(self, step):
        """
        执行js代码
        """
        self.driver.execute_script(step["data"])

    #键鼠常用操作:双击，右击，悬停，拖拽，回车
    @kw_step
    def double_click(self, step):
        """
        双击
        """
        element=self.find(step)
        action=ActionChains(self.driver)
        action.double_click(element).perform()

    @kw_step
    def right_click(self, step):
        """
        右击
        """
        element = self.find(step)
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    @kw_step
    def hover(self, step):
        """
        悬停
        """
        element = self.find(step)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @kw_step
    def drag_and_drop(self, step):
        """
        拖拽
        step["data"]数据要写成字典{'by':'xpath','value':'xxx'}形式
        """
        source=self.find(step)
        target_dict=eval(step["data"])
        target=self.driver.find_element(target_dict["by"], target_dict["value"])
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    @kw_step
    def enter(self, step):
        """
        回车
        """
        element = self.find(step)
        element.send_keys(Keys.ENTER)

    #文件上传
    @kw_step
    def upload(self, step):
        """
        上传文件
        """
        relative_path=step["data"]
        absolute_path=os.path.abspath(relative_path)
        element = self.find(step)
        element.send_keys(absolute_path)

    #frame操作：切换到某个frame，切换主文档

    @kw_step
    def switch_to_frame(self,step):
        """根据frame元素把焦点切换到某个frame"""
        element=self.find(step)
        self.driver.switch_to_frame(element)

    @kw_step
    def switch_to_default_content(self, step):
        """把焦点切换回主文档"""
        self.driver.switch_to_default_content()
