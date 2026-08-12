#driver相关配置项

#浏览器类型：chrome/edge
BROWSER_TYPE = "chrome"
#使用哪种浏览器驱动管理方式：local/其他
DRIVER_TYPE = "local"
#本地浏览器驱动路径
CHROME_DRIVER_PATH = "./driver/chromedriver.exe"
EDGE_DRIVER_PATH = "./driver/edgedriver.exe"
#是否开启无头模式
HEADLESS=False
#excel测试用例地址
EXCEL_FILE="./data/测试用例.xlsx"

# #mysql配置
# DB_HOST="192.168.10.131"
# DB_PORT=3306
# DB_NAME="mydb"
# DB_USER="root"
# DB_PASSWORD="123456"
# #sql资源销毁
# SQL1='delete from sp_categoty where cat_name="大码服装"'
# SQL2='delete from sp_categoty where attr_name="VIP尺码"'