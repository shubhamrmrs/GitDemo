from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    productButton = (By.XPATH, "//div[@class='card h-100']/div/button")
    goToCheckoutButton = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
    checkoutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductName(self):
        return self.driver.find_elements(*CheckoutPage.productName)

    def getProductButton(self):
        return self.driver.find_elements(*CheckoutPage.productButton)

    def getGoToCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.goToCheckoutButton)

    def getCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage



