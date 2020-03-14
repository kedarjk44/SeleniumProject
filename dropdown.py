from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\setups\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.find_element_by_id("tab-car-tab-hp").click()
drp_box = Select(driver.find_element_by_id("car-pickup-time-hp-car"))
drp_box.select_by_visible_text("8:15 am")

drp_box = Select(driver.find_element_by_id("car-dropoff-time-hp-car"))
drp_box.select_by_visible_text("10:45 am")

