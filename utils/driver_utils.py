import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import BROWSER_TYPE, HEADLESS, DRIVER_TYPE, CHROME_DRIVER_PATH
from selenium.webdriver.edge.service import Service as EdgeService


#根据配置项实现：创建哪种浏览器对象，使用哪种管理驱动方式，是否开启无头模式

def get_driver():
    driver=None
    if BROWSER_TYPE == "chrome":
        driver=get_chrome_driver()
    if BROWSER_TYPE == "edge":
        driver=get_chrome_driver()

    return driver


def get_chrome_driver():
    #浏览器参数设置
    options=webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless") if HEADLESS else None

    #判断使用哪种驱动
    if DRIVER_TYPE =="local":
        service=Service(CHROME_DRIVER_PATH)
    else:
        service=Service(ChromeDriverManager().install())

    driver=webdriver.Chrome(service=service,options=options)

    logging.info("启动chrome浏览器成功")
    return driver



def get_edge_driver():
    # 浏览器参数设置
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless") if HEADLESS else None

    # 判断使用哪种驱动
    if DRIVER_TYPE == "local":
        service = EdgeService(CHROME_DRIVER_PATH)
    else:
        service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    logging.info("启动edge浏览器成功")
    return driver