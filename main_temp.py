# Main executable file
import database
import pprint
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.product_comparison_table import ComparisonTable
from lib.saveonfood import SaveOnFoodPage

def main():
  driver = webdriver.Chrome()
  sp = SaveOnFoodPage(driver)
  try: 
    sp.search("apple")
    saveonfood_list = sp.getAllSearchedlProducts()

    for item in saveonfood_list:
      pprint.pprint(item.exportJSON())

    sp.search("singer singer")
    saveonfood_list = sp.getAllSearchedlProducts()

    for it in saveonfood_list:
      pprint.pprint(it.exportJSON())

  except Exception as e:
    print(e)

  # End the browser
  driver.quit()

if __name__ == "__main__":
  main()