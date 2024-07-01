from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    autoSuggestiveCheckBox = (By.ID, "country")
    countrySelection = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    alertMessage = (By.CLASS_NAME, "alert-success")

    def getAutoSuggestiveCheckBox(self):
        return self.driver.find_element(*ConfirmPage.autoSuggestiveCheckBox)

    def getCountrySelection(self):
        return self.driver.find_element(*ConfirmPage.countrySelection)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alertMessage)
