from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .base import BasePage
from .superstore_locator import Locators
from datetime import datetime
from models.superstore_product import SuperStoreProduct

def try_find_element(element, name, get_text):
  try:
    prod = element.find_element_by_class_name(name)
    if(get_text):
      return prod.text
    else:
      return prod
  except:
    return ""

class SuperStorePage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    # Open browser
    self.driver.get("https://www.realcanadiansuperstore.ca/search")

  # Search in input bar
  def search(self, text):
    self.locateElement(Locators.SEARCH_TEXTBOX).clear()
    self.enter_text(Locators.SEARCH_TEXTBOX, text)
    self.enter_text(Locators.SEARCH_TEXTBOX, Keys.RETURN)

  # After searched
  def getAllSearchedlProducts(self):
    try:
      group = self.locateElement(Locators.PRODUCT_TILE_GROUP_LIST)
      product_grid = group.find_elements_by_class_name("product-tracking")
      product_list = []
      count = 0
      for li in product_grid:
        # print("source: ", li.get_attribute("outerHTML"))
        product_name = try_find_element(li, Locators.PRODUCT_NAME[1], True)
        product_price = try_find_element(li, Locators.PRODUCT_PRICE[1], True)
        product_unit = try_find_element(li, Locators.PRODUCT_UNIT[1], True)
        product_is_on_sale = try_find_element(li, Locators.PRODUCT_IS_ON_SALE[1], True)
        product_comparison_price = try_find_element(li, Locators.PRODUCT_COMPARISON_PRICE[1], True)
        product_comparison_unit = try_find_element(li, Locators.PRODUCT_COMPARISON_UNIT[1], True)
        product_list.append(
          SuperStoreProduct(product_name,product_price, 
          product_unit, product_is_on_sale, product_comparison_price, product_comparison_unit)
        )
        count += 1
        if(count == 1):
          break
      return product_list
    except:
      return []
    
    