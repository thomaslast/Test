from selenium import webdriver
from selenium.webdriver.common.keys import Keys
search = "testing"
driver = webdriver.Firefox()
driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_id("searchform")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
driver.close()