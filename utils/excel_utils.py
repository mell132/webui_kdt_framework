import openpyxl

from config.config import *

def read_excel(file_path=EXCEL_FILE,sheet_name=SHEET_NAME):
    #打开excel文件
    workbook=openpyxl.load_workbook(file_path)
    #读数操作
    data=[]
    #由于有合并单元格的问题，我们可以把所有数据读出来，进行筛选，合格的用例才添加到data中

    all_cases=[]

    #定义当前用例数据,组织处理每条用例处理的问题
    current_case=None

    # worksheet=workbook[sheet_name]--这次需要遍历多个sheet
    for worksheet in workbook.worksheets:
        keys=[cell.value for cell in worksheet[2]]
        for row in worksheet.iter_rows(min_row=3, values_only=True): #从第三行开始，只返回值
            dict_data=dict(zip(keys, row))
            #只要id不为None，代表这是一条用例
            if dict_data["id"] is not None:
                #组织用例过程
                current_case={
                    "id":dict_data["id"],
                    "feature":dict_data["feature"],
                    "story":dict_data["story"],
                    "title":dict_data["title"],
                    "steps":[
                        {
                            "step_num":dict_data["step_num"],
                            "step_name":dict_data["step_name"],
                            "keyword":dict_data["keyword"],
                            "by":dict_data["by"],
                            "value":dict_data["value"],
                            "data":dict_data["data"],
                            "index":dict_data["index"]
                        }
                    ],
                    "is_true":dict_data["is_true"],

                }
                #临时存起来，存到all_case中
                all_cases.append(current_case)
            #id为None的情况下,一般就是步骤，确保有当前用例数据的情况下，把步骤添加进去
            elif current_case is not None:
                current_case["steps"].append(
                    {

                        "step_num":dict_data["step_num"],
                        "step_name":dict_data["step_name"],
                        "keyword":dict_data["keyword"],
                        "by":dict_data["by"],
                        "value":dict_data["value"],
                        "data":dict_data["data"],
                        "index":dict_data["index"]

                })
    data=[case for case in all_cases if case["is_true"]]
    print(all_cases)
    print(data)
    #关闭excel
    workbook.close()
    return data

# read_excel()