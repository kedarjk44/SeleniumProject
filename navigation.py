from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path="C:\setups\chromedriver.exe")

driver.get("http:/newtours.demoaut.com/")
print(driver.title)
sleep(5)
driver.get("http:/demo.automationtesting.in/Windows.html")
print(driver.title)
sleep(5)
driver.back()
sleep(5)
print(driver.title)
driver.forward()
sleep(5)
print(driver.title)
driver.close()

