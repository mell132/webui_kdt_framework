import pytest
import os

if __name__ == "__main__":
    #4进程
    #pytest.main(["-vs", "-n4", "./testcases/test_runner.py", "--alluredir", "./report/json_report", "--clean-alluredir"])
    pytest.main(["-vs","./testcases/test_runner.py","--alluredir","./report/json_report","--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")
