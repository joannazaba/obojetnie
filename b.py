from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""
alq mq wwrd eferfrtet kota
"""

@Given('PrimeFaces page')
def step_impl(context):
	context.driver.get("http://www.primefaces.org/showcase/ui/ajax/dropdown.xhtml")

@When('select "country"')
def step_impl(context):
	element = context.driver.find_element_by_xpath("//*[@id='j_idt87:country_label']")
	element.click()
	element2 = context.driver.find_element_by_xpath("//*[@data-label='USA']")
	element2.click()
	
@When('select "city"')
def step_impl(context):
	#time.sleep(1)
	wait = WebDriverWait(context.driver, 1)
	element0 = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@data-label='Denver']")))
	element = context.driver.find_element_by_xpath("//*[@id='j_idt87:city_label']")
	element.click()
	element2 = context.driver.find_element_by_xpath("//*[@data-label='Denver']")
	element2.click()