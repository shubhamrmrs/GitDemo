from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    name = (By.CSS_SELECTOR, "input[name='name']")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    submitButton = (By.XPATH, "//input[@value='Submit']")
    message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getRadio(self):
        return self.driver.find_element(*HomePage.radio)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
