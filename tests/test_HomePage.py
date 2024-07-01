import time

import pytest
from testData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_FormSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Name is " + getData["Name"])

        homepage.getName().send_keys(getData["Name"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPassword().send_keys(getData["Password"])
        homepage.getCheckBox().click()

        self.selectOptionByText(homepage.getGender(), getData["Gender"])

        homepage.getRadio().click()
        homepage.getSubmitButton().click()
        msg = homepage.getMessage().text
        print(msg)

        assert "Success" in msg
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("5th_Test"))
    def getData(self, request):
        return request.param
