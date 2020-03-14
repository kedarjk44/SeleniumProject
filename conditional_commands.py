from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome(executable_path="C:\setups\chromedriver.exe")

driver.get("http:/newtours.demoaut.com/")
elm = driver.find_element_by_name("userName")
print(elm.is_displayed())
print(elm.is_enabled())

pswd = driver.find_element_by_name("password")
print(pswd.is_displayed())
print(pswd.is_enabled())

elm.send_keys("mercury")
pswd.send_keys("mercury")

driver.find_element_by_name("login").click()
sleep(5)
# round_trip = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[1]")
round_trip = driver.find_element_by_css_selector("input[value=roundtrip]")
print(round_trip.is_displayed())
print(round_trip.is_selected())

one_trip = driver.find_element_by_css_selector("input[value=oneway]")
print(one_trip.is_selected())

driver.close()

