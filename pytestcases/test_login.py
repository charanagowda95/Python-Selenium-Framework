import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from testcases import conftest
from pageobjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

'''filename,classname (test_,Test_,and testcase/method name should start with "test_"
>pytest -v -s testcases\test_login.py --browser firefox
>pytest -v -s -n=3 testcases\test_login.py --browser firefox---->parallel
>pytest -v -s --html=.\reports\report.html testcases\test_login.py --browser firefox
>pytest -v -s -m "sanity" testcases\test_login.py --browser chrome
>pytest -v -s -m "sanity or smoke" testcases\test_login.py --browser chrome
>pytest -v -s -m "sanity and smoke" testcases\test_login.py --browser chrome
>pytest -v -s -n=2 --html=reports\report.html -m "sanity and smoke" testcases\test_login.py --browser chrome

'''


class Test_Login:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()
    homepagetitle = ReadConfig.getHomePageTitle()
    loginpagetitle = ReadConfig.getLoginPageTitle()
    path = '.\\TestData\\LoginData.xlsx'

    logger = LogGen.getlogger()

    @pytest.mark.sanity
    def test_001(self, setup):
        self.logger.info("test started tc001")
        self.driver = setup
        self.driver.get(self.base_url)
        acttitle = self.loginpagetitle
        exptitle = self.driver.title
        self.driver.close()
        if acttitle == exptitle:
            assert True
            self.logger.info("tc001 passed")
        else:
            self.logger.error("tc001 failed")
            self.driver.save_screenshot(".\\screenshots\\" + "test.png")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    def test_002(self, setup):
        self.logger.info("tc002 started")
        self.driver = setup
        self.driver.get(self.base_url)
        acttitle = self.loginpagetitle
        exptitle = self.driver.title
        if acttitle == exptitle:
            assert True
        else:
            self.logger.info("tc002 failed")
            self.driver.close()
            assert False
        lp = LoginPage(self.driver)
        lp.setUn(self.username)
        lp.setPwd(self.password)
        lp.click_sub()
        acthometitle = self.homepagetitle
        exphometitle = self.driver.title
        self.driver.close()

        if acthometitle == exphometitle:
            assert True
            self.logger.info("tc002 passed")
        else:
            self.logger.info("tc002 fialed")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_003(self, setup):
        self.logger.info("tc002 started")
        self.driver = setup
        self.driver.get(self.base_url)
        acttitle = self.loginpagetitle
        exptitle = self.driver.title
        if acttitle == exptitle:
            assert True
        else:
            self.logger.info("tc002 failed")
            self.driver.close()
            assert False
        lp = LoginPage(self.driver)
        lp.setUn(self.username)
        lp.setPwd(self.password)
        lp.click_sub()
        acthometitle = self.homepagetitle
        exphometitle = self.driver.title
        self.driver.close()

        if acthometitle == exphometitle:
            assert True
            self.logger.info("tc002 passed")
        else:
            self.logger.info("tc002 fialed")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_datadriven(self, setup):

        self.logger.info("test started tc001")
        self.driver = setup
        self.driver.get(self.base_url)
        self.rows = XLUtils.get_row_count(self.path, "data")
        list_status = []  # emotylist
        for r in range(2, self.rows + 1):
            self.un = XLUtils.read_data(self.path, "data", r, 1)
            self.pwd = XLUtils.read_data(self.path, "data", r, 2)
            self.exp = XLUtils.read_data(self.path, "data", r, 3)
            lp = LoginPage(self.driver)
            lp.setUn(self.un)
            lp.setPwd(self.pwd)
            lp.click_sub()
            acthometitle = self.homepagetitle
            exphometitle = self.driver.title

            if acthometitle == exphometitle:
                if self.exp == "pass":
                    assert True
                    self.logger.info("passed")
                    list_status.append("pass")

                elif self.exp == "fail":
                    assert False
                    self.logger.info("failed")
                    list_status.append("fail")

            elif acthometitle != exphometitle:
                if self.exp == "pass":
                    assert False
                    self.logger.info("failed")
                    list_status.append("fail")


                elif self.exp == "fail":
                    assert True
                    self.logger.info("passed")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("datadriven is passed")
        else:
            self.logger.info("datadriven failed")

        self.driver.close()
