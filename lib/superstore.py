from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .base import BasePage
from .superstore_locator import Locators

class SuperStorePage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    # Open browser
    self.driver.get("https://www.realcanadiansuperstore.ca")

  # Search in input bar
  def search(self, text):
    self.locateElement(Locators.SEARCH_TEXTBOX).clear()
    self.enter_text(Locators.SEARCH_TEXTBOX, text)
    self.enter_text(Locators.SEARCH_TEXTBOX, Keys.RETURN)

  # After searched
  def getAlSearchedlProducts(self):
    group = self.locateElement(Locators.PRODUCT_TILE_GROUP_LIST)
    product_grid = group.find_elements_by_class_name("product-tracking")
    product_list = []
    for li in product_grid:
      # print("source: ", li.get_attribute("outerHTML"))
      product_name = li.find_element_by_class_name(Locators.PRODUCT_NAME[1]).text
      product_price = li.find_element_by_class_name(Locators.PRODUCT_PRICE[1]).text
      product_unit = li.find_element_by_class_name(Locators.PRODUCT_UNIT[1]).text
      product_list.append({
        "product_name": product_name,
        "product_price": product_price,
        "product_unit": product_unit
      })
    return product_list