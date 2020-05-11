import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from selenium import webdriver
from utilities.customLogger import LogGen

class Test_001_Login:
    # baseURL = "https:/admin-demo.nopcommerce.com"
    # username = "admin@yourstore.com"
    # password = "admin"
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    #driver=webdriver.Chrome()

    @pytest.mark.regression

    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login ************ ")
        self.logger.info("************** Started home page title test ************ ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title =="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************** Home PageTitle test is passed ************ ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Home PageTitle test is failed ************ ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self,setup):
        self.logger.info("************** Login Test is started ************ ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login test test is passed ************ ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************** Login test is failed ************ ")
            assert False
