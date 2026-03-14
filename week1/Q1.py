from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("harshita@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys("12345")
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()
sleep(2)

driver.close()
driver.quit()


