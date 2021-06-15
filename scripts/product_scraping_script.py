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

def run(ProductClass, ProductPage, brand, times=None):
  driver = webdriver.Chrome()
  sp = ProductPage(driver)

  try: 
    database.connectMongoClient()
    product_collection = database.getCollection("products")
    superstore_collection = database.getCollection("store_products")
    comparison_collection = database.getCollection("comparison_tables")

    # Pull data from product
    all_products = database.findAll(product_collection, {})

    count = 0
    for prod in all_products:

      # let's find existed comparison object first
      found_comp = database.findOne(comparison_collection, {'product': prod['_id']})
      
      # If found -> We check for store_product and try to find the brand
      if(found_comp is not None):

        # Find store product within the comparison object 
        found_store = try_find_store_product(found_comp['store_product'], brand)

        if(found_store is None): # We add new data to the array and insert back
          existed_store_arr = found_comp['store_product']
          superstore_inserted = insert_to_store_mongo(sp, prod, superstore_collection, ProductClass, brand)
          existed_store_arr.append(superstore_inserted.inserted_id)
          database.updateOne(comparison_collection, {"_id": found_comp['_id']}, {"$set": {"store_product": existed_store_arr}})

        else: # In here if we found the brand, we need to check for the lock status
          if((found_store['locked'] is None) or (found_store['locked']== False)):
            update_existed_store(sp, prod, superstore_collection, found_store)
          else:
            update_existed_store_using_store_name(sp, prod, superstore_collection, found_store)

      else: # Insert new one into the mongo
        superstore_inserted = insert_to_store_mongo(sp,prod, superstore_collection, ProductClass, brand)
        # Create comparison and insert
        compare_table = ComparisonTable(prod['_id'], superstore_inserted.inserted_id)
        database.insertOne(comparison_collection, compare_table.exportJSON())

      time.sleep(1.5)
      count += 1

      print("Completed product number ", count)
      if(times is not None):
        if(count == times):
          break

    database.closeClient()

  except Exception as e:
    print("exception: ", e)
    driver.quit()

  # End the browser
  driver.quit()

def searchProduct(sp, name=""):
  sp.search(name)
  superstore_list = sp.getAllSearchedlProducts()
  return superstore_list

def try_find_store_product(store_arr, brand):
  superstore_collection = database.getCollection("store_products")
  for each_id in store_arr:
    found_store = database.findOne(superstore_collection, {'_id': each_id})
    if(found_store is not None):
      store_brand = found_store['brand']
      if(store_brand == brand):
        return found_store
  return None

def insert_to_store_mongo(sp, ditu_product, superstore_collection, ProductClass, brand):
  # If have any product connect to mongodb
  superstore_list = searchProduct(sp, ditu_product['name'])
  if(len(superstore_list) > 0):
    for su in superstore_list:
      # Insert to superstore model
      su.setProduct(ditu_product['_id'])
      superstore_inserted = database.insertOne(superstore_collection, su.exportJSON())
      return superstore_inserted
  else:
    # Create an empty object
    obj = ProductClass()
    obj.setBrand(brand)
    obj.setProduct(ditu_product['_id'])
    # Insert into superstore with empty object
    superstore_inserted = database.insertOne(superstore_collection, obj.exportJSON())
    return superstore_inserted

def update_existed_store(sp, ditu_product, superstore_collection, found_store):
  superstore_list = searchProduct(sp, ditu_product['name'])
  for su in superstore_list:
    su.setProduct(ditu_product['_id'])
    database.updateOne(superstore_collection, {"_id": found_store['_id']}, {"$set": su.exportJSON()})

def update_existed_store_using_store_name(sp, ditu_product, superstore_collection, found_store):
  up = found_store['updated']
  if((up is not None) and (up is True)):
    superstore_list = searchProduct(sp, found_store['name'])
    for su in superstore_list:
      su.setProduct(ditu_product['_id'])
      su.setLocked(True)
      su.setUpdated(True)
      database.updateOne(superstore_collection, {"_id": found_store['_id']}, {"$set": su.exportJSON()})