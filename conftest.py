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

