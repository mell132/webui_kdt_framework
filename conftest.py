import time

import pymysql
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from config.config import *
from utils.driver_utils import get_driver


@pytest.fixture(scope="function")
def driver_handler():

    #创建浏览器对象
    driver = get_driver()

    yield driver

    #关闭浏览器对象
    driver.quit()

#pytest_runtest_makereport是pytest内置的钩子函数，自动执行，用于生成测试用例的执行结果

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    #item:测试用例对象本身，包括测试类，参数化信息，标记，所在文件路径等
    #call:测试用例执行过程信息，包括执行阶段，执行开始和结束时间，执行结果等
    outcome = yield
    res=outcome.get_result()
    #如果执行过程中发现执行失败了
    if res.when =="call" and res.failed:
        params=item.funcargs
        driver=params.get("driver_handler")
        now_time=time.strftime("%Y-%m-%d %H:%M:%S")
        png_name=f'./screenshots/失败截图_{params["case"]["id"]}_{now_time}.png'
        driver.save_screenshot(png_name)





