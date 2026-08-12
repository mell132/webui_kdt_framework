import time
class Keywords:

    def __init__(self,driver):
        self.driver=driver

    def open(self,a,b,c):
        self.driver.get(c)

    def input(self,a,b,c):
        self.driver.find_element(a,b).send_keys(c)

    def wait(self,a,b,c):
        time.sleep(c)
