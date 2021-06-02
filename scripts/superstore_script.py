# This is full script for browsing Canadian Superstore
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import database
import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.product_comparison_table import ComparisonTable
from lib.superstore import SuperStorePage

def run(times=None):
  driver = webdriver.Chrome()
  sp = SuperStorePage(driver)
  try: 
    database.connectMongoClient()
    product_collection = database.getCollection("products")
    superstore_collection = database.getCollection("store_products")
    comparison_collection = database.getCollection("comparison_tables")

    # Pull data from product
    all_products = database.findAll(product_collection, {})

    count = 0
    for prod in all_products:

      # Search for search bar
      sp.search(prod['name'])
      superstore_list = sp.getAllSearchedlProducts()

      # If have any product connect to mongodb
      if(len(superstore_list) > 0):
        for su in superstore_list:
          print(su)
          # Insert to superstore model
          superstore_inserted = database.insertOne(superstore_collection, su.exportJSON())
          # Create comparision table object
          compare_table = ComparisonTable(prod['_id'], superstore_inserted.inserted_id)
          database.insertOne(comparison_collection, compare_table.exportJSON())
      else:
        compare_table = ComparisonTable(prod['_id'], None)
        database.insertOne(comparison_collection, compare_table.exportJSON())

      time.sleep(1.5)
      count += 1

      print("Completed product number ", count)
      if(times is not None):
        if(count == times):
          break
    
    database.closeClient()

  except Exception as e:
    print(e)
    driver.quit()

  # End the browser
  driver.quit()