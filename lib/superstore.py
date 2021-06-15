from selenium.webdriver.common.keys import Keys
from .base import BasePage
from .superstore_locator import Locators
from datetime import datetime
from models.product import Product

def try_find_element(element, name, get_text):
  try:
    prod = element.find_element_by_class_name(name)
    if(get_text):
      return prod.text
    else:
      return prod
  except:
    return ""

def try_find_image(element, name):
  try:
    prod = element.find_element_by_class_name(name)
    return prod.get_attribute("src")
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
      product_grid = group.find_elements_by_class_name(Locators.PRODUCT_TRACKING[1])
      product_list = []
      count = 0
      for li in product_grid:
        # print("source: ", li.get_attribute("outerHTML"))
        product_name = try_find_element(li, Locators.PRODUCT_NAME[1], True)
        product_price = try_find_element(li, Locators.PRODUCT_PRICE[1], True)
        product_unit = try_find_element(li, Locators.PRODUCT_UNIT[1], True)
        product_image = try_find_image(li, Locators.PRODUCT_IMAGE[1])
        product_is_on_sale = try_find_element(li, Locators.PRODUCT_IS_ON_SALE[1], True)
        product_comparison_price = try_find_element(li, Locators.PRODUCT_COMPARISON_PRICE[1], True)
        product_comparison_unit = try_find_element(li, Locators.PRODUCT_COMPARISON_UNIT[1], True)
        product_list.append(
          Product(product_name,product_image, product_price, 
          product_unit, product_is_on_sale, product_comparison_price, product_comparison_unit, "", False, "superstore")
        )
        count += 1
        if(count == 1):
          break
      return product_list
    except:
      return []
    
    