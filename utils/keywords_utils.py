import allure
import logging

def kw_step(func):
    """
    装饰器，用于记录allure步骤和日志信息
    """
    def wrapper(self,step):
        #记录allure步骤
        with allure.step(f'第{step["step_num"]}步：{step["step_name"]}'):

            logging.info(f'第{step["step_num"]}步：{step["step_name"]}-元素（{step['by']},{step['value']}）-数据（{step["data"]}）-索引({step["index"]})')

            return func(self,step)
    return wrapper