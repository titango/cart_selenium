# Main executable file
from lib.superstore import SuperStorePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import database
import pprint

def main():
  print("Staring program in main")
  
  # Driver from chrome
  driver = webdriver.Chrome()
  sp = SuperStorePage(driver)
  
  # pageSource = driver.page_source

  try: 
    database.connectMongoClient()
    product_collection = database.getCollection("products")

    # Pull data from product
    all_products = database.findAll(product_collection, {})

    for prod in all_products:

      # Search for search bar
      sp.search(prod.name)
      superstore_list = sp.getAllSearchedlProducts()

      # If have any product connect to mongodb
      if(len(superstore_list) > 0):
        
        superstore_collection = database.getCollection("superstore_products")
        for su in superstore_list:
          database.insertOne(superstore_collection, su.exportJSON())

        database.closeClient()

  except Exception as e:
    print(e)
    driver.quit()

  # End the browser
  driver.quit()

if __name__ == "__main__":
  main()