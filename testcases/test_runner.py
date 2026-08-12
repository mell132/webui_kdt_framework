import logging
import pytest
from jinja2 import Template

from core import assert_keywords
from core.assert_keywords import AssertKeywords
from utils.allure_utils import allure_init
from utils.excel_utils import read_excel

from core.keywords import Keywords


class TestRunner:
    #读取测试用例文件中的全部数据，用属性保存
    data=read_excel()

    # #提取后的数据需要初始化一个全局的属性来保存，可以使用{}空字典
    # all={}

    @pytest.mark.parametrize("case",data)
    def test_case(self,case,driver_handler):

        # all=self.all
        # #引用全局变量，根据all的值渲染case
        # case=eval(Template(str(case)).render(all))

        #初始化allure报告
        allure_init(case)

        #测试用例的描述信息
        logging.info(f"用例ID:{case["id"]} 模块：{case["feature"]} 场景：{case["story"]} 标题：{case["title"]}")
        #创建浏览器
        #创建关键字对象
        keywords=Keywords(driver_handler)
        assert_keywords=AssertKeywords(driver_handler)
        #执行
        for step in case["steps"]:

            #记录步骤的描述信息日志
            #匹配关键字：A.__getattribute__(属性名或方法名)-返回一个绑定方法对象类型的数据
            for i in [keywords,assert_keywords]:
                if hasattr(i,step["keyword"]):
                    func_name = i.__getattribute__(step["keyword"])
                    func_name(step)
                    break
            else:
                raise AssertionError(f"❌️没有找到关键字：{step['keyword']}")






