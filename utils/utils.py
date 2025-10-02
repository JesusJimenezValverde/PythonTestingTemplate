
class Utils:
    def __init__(self, driver):
        self.driver = driver

    # def accept_alert(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 10)
    #         alert = wait.until(EC.alert_is_present())
    #         alert.accept()
    #         print("Alert Accepted")
    #     except TimeoutException:
    #         print("No alert was present.")