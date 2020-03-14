from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\setups\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.expedia.com/")
print(driver.title)
print(driver.current_url)
assert driver.current_url == "https://www.expedia.com/", "Error occurred"

driver.find_element_by_id("tab-flight-tab-hp").click()
# from_flight_list = ["SFO", "NYC", "LA", "LV"]
# to_flighs = ["SFO", "NYC", "LA", "LV"]
# for i in range(len(from_flight_list)):
#     from_flight = from_flight_list[i]
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")

driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("02/18/2020")
# driver.f

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("02/19/2020")

driver.find_element_by_id("flight-add-hotel-checkbox-flp").click()

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

wait = WebDriverWait(driver, 30)

elm = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
elm.click()
sleep(3)
elm2 = wait.until(EC.element_to_be_clickable((By.ID, "airlineRowContainer_UA")))
elm2.click()
sleep(5)
elm3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='flight-module-2020-02-18t09:15:00-08:00-coach-sfo-ewr-ua-2065_2020-02-18t20:59:00-05:00-coach-ewr-sfo-ua-1526_']/div[1]/div[1]/div[1]/div/div/div/div[1]/div[3]/a")))
elm3.click()
sleep(2)
driver.find_element_by_css_selector("input[value=ONE_WAY]").click()
sleep(2)
driver.find_element_by_id("primary-header-car").click()
sleep(5)
print(driver.title)
print(driver.current_url)
driver.back()
print(driver.title)
print(driver.current_url)
# driver.quit()
# driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[7]/label/button").click()
# /html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[7]/label/button
driver.close()
