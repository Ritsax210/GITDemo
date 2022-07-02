from selenium import webdriver  # importing of packages
#from selenium.webdriver.common.keys import Keys  #importing of packages
import time

driver = webdriver.Chrome(executable_path='C:/Users/rsaxena/AppData/Local/Programs/Python/Python310/chromedriver_win32/chromedriver.exe')
driver.get("https://test.salesforce.com/")
print(driver.title)  # title of the page
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='forgot_password_link']").click()
time.sleep(5)
#driver.close()  # close the browser
