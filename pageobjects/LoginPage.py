from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class LoginPage:
    un_box_name="user_name"
    pwd_box_name="user_password"
    sub_btn_id="submitButton"

    def __init__(self,driver):
        self.driver=driver

    def setUn(self,un):
        une=self.driver.find_element_by_name(self.un_box_name)
        une.clear()
        une.send_keys(un)
    def setPwd(self,pwd):
        pwde= self.driver.find_element_by_name(self.pwd_box_name)
        pwde.clear()
        pwde.send_keys(pwd)
    def click_sub(self):
        self.driver.find_element_by_id(self.sub_btn_id).click()