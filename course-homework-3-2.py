class Saucedemo:

    def testcase1(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from time import sleep
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.find_element(By.NAME, "user-name").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        driver.find_element(By.NAME, "login-button").click()
        print("Error: " + driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text)

    def testcase2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from time import sleep
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.find_element(By.NAME, "user-name").send_keys("...")
        driver.find_element(By.NAME, "password").send_keys("")
        driver.find_element(By.NAME, "login-button").click()
        print("Error: " + driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text)

    def testcase3(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from time import sleep
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.find_element(By.NAME, "user-name").send_keys("locked_out_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        print("Error: " + driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text)

    def testcase4(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from time import sleep
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.find_element(By.NAME, "user-name").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        driver.find_element(By.NAME, "login-button").click()
        sleep(1)
        driver.find_element(By.CLASS_NAME, "error-button").click()
        sleep(5)

    def testcase5(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from time import sleep
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        sleep(1)
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.NAME, "login-button").click()
        sleep(5)

    def testcase6(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from time import sleep
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        sleep(1)
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.NAME, "login-button").click()
        sleep(2)
        print(len(driver.find_elements(By.CLASS_NAME, "inventory_item")))



saucedemo = Saucedemo()
saucedemo.testcase1()
saucedemo.testcase2()
saucedemo.testcase3()
saucedemo.testcase4()
saucedemo.testcase5()
saucedemo.testcase6()
