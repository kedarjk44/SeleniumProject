from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="C:\setups\chromedriver.exe")
# driver.get("http://newtours.demoaut.com/")
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
# driver.close()

driver.get("http:/demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()
sleep(3)
driver.close()
driver.quit()

fox_driver = webdriver.Firefox(executable_path="C:\setups\geckodriver.exe")
fox_driver.get("http://newtours.demoaut.com/")
print(fox_driver.title)
fox_driver.close()
fox_driver.quit()

# ie_driver = webdriver.Ie(executable_path="D:\setups\IEDriverServer_x64_3.9.0\IEDriverServer.exe")
# ie_driver.get("http://newtours.demoaut.com/")
# print(ie_driver.title)
# ie_driver.close()
