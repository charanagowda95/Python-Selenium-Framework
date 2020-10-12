import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from testcases import conftest
from pageobjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_Login:
    base_url = ReadConfig.getApplicationUrl()
    logger = LogGen.getlogger()
    homepagetitle = ReadConfig.getHomePageTitle()
    loginpagetitle = ReadConfig.getLoginPageTitle()
    path = '.\\TestData\\LoginData.xlsx'

    def test_datadriven(self, setup):
        self.logger.info("test started tc001")
        self.driver = setup
        self.driver.get(self.base_url)
        self.rows = XLUtils.get_row_count(self.path, "data")
        list_status = []  # emotylist
        for i in range(2, self.rows + 1):
            self.username = XLUtils.read_data(self.path, "data", i, 1)
            self.password = XLUtils.read_data(self.path, "data", i, 2)
            self.exp = XLUtils.read_data(self.path, "data", i, 3)
            lp = LoginPage(self.driver)
            lp.setUn(self.username)
            lp.setPwd(self.password)
            lp.click_sub()
            acthometitle = self.homepagetitle
            exphometitle = self.driver.title

            if acthometitle == exphometitle:
                if self.exp == "pass":
                    self.logger.info("passed")
                    list_status.append("pass")


                elif self.exp == "fail":
                    self.logger.info("failed")
                    list_status.append("fail")



            elif acthometitle != exphometitle:
                if self.exp == "pass":
                    self.logger.info("failed")
                    list_status.append("fail")

                elif self.exp == "fail":
                    self.logger.info("passed")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("datadriven is passed")
        else:
            self.logger.info("datadriven failed")
        self.driver.close()
