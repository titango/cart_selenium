from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

  def __init__(self, driver):
    self.driver=driver

  def click(self, locator):
    return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

  def enter_text(self, locator, text):
    return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

  def hover_to(self, locator):
    element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    ActionChains(self.driver).move_to_element(element).perform()

  def is_visible(self,locator):
    element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    return bool(element)

  def locateElement(self, locator):
    return WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))