#Automate Text Field Entry Using ID Locator
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.naukri.com/")
driver.maximize_window()
sleep(3)

driver.find_element(By.LINK_TEXT,"Register").click()
sleep(3)
driver.find_element(By.ID,"name").send_keys("Harshita Yadav")
driver.find_element(By.ID,"email").send_keys("harshita@gmail.com")
driver.find_element(By.ID,"password").send_keys("Harshita123")

sleep(3)
driver.close()
driver.quit()
