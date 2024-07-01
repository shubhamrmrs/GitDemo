import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_1(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homepage = HomePage(self.driver)

        checkoutPage = homepage.shopItems()
        log.info("Getting all the product titles")
        products = checkoutPage.getProductName()
        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getProductButton()[i].click()
        checkoutPage.getGoToCheckoutButton().click()

        confirmPage = checkoutPage.getCheckoutButton()
        log.info("Entering country name as ind")
        confirmPage.getAutoSuggestiveCheckBox().send_keys("ind")

        self.verifyLinkPresence("India")

        confirmPage.getCountrySelection().click()
        confirmPage.getCheckBox().click()
        confirmPage.getPurchaseButton().click()
        msg = confirmPage.getAlertMessage().text
        log.info("text received from application is " + msg)

        assert "Success! Thank you!" in msg
        print("GIT changes done")
        print("GIT changes done")
        print("GIT changes done")

        time.sleep(2)
