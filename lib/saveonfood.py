from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime

from .base import BasePage
from .saveonfood_locator import Locators
from models.saveonfood_product import SaveOnFoodProduct

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

class SaveOnFoodPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    # Open browser
    self.driver.get("https://www.saveonfoods.com/sm/pickup/rsid/987/")

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
        product_name = product_name.replace("Open product description", "")

        product_price_unit = try_find_element(li, Locators.PRODUCT_PRICE[1], True)
        converted = convert_product_price_unit(product_price_unit)
        product_price = converted[0]
        product_unit = converted[1]

        product_image = try_find_image(li, Locators.PRODUCT_IMAGE[1])
        product_is_on_sale = False

        product_comparison_price_unit = try_find_element(li, Locators.PRODUCT_COMPARISON_PRICE[1], True)
        com_converted = convert_comparison_price_unit(product_comparison_price_unit)
        product_comparison_price = com_converted[0]
        product_comparison_unit = com_converted[1]

        product_list.append(
          SaveOnFoodProduct(product_name,product_image, product_price, 
          product_unit, product_is_on_sale, product_comparison_price, product_comparison_unit, "saveonfood")
        )
        count += 1
        if(count == 1):
          break
      return product_list
    except Exception as e:
      print(e)
      return []
  
def convert_product_price_unit(prod_price_unit):
  if(prod_price_unit.find('/') != -1): # Does not have -> price fix
    s = prod_price_unit.split("/")
    price = s[0].replace("avg", "")
    unit = s[1]
    return (price, unit)
  else:
    return (prod_price_unit, "")

def convert_comparison_price_unit(comparison_price_unit):
  if(comparison_price_unit.find("/") != -1): # Let's find with pattern 'X/Y' first
    s = comparison_price_unit.split("/")
    return(s[0], s[1])
  elif (comparison_price_unit.find("each") != -1): # Let's find with pattern 'X each'
    s = comparison_price_unit.split("each")
    return(s[0], "each")
  else:
    return("","")
    
  