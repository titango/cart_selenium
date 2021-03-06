# PYTHON MODEL FOR SUPERSTORE PRODUCT
from datetime import datetime

class Product():
  def __init__(self, name="", image="", price="", unit="", is_on_sale=False, product_comparison_price="", 
  product_comparison_unit="", product="", updated=False, brand=""):
    if((is_on_sale is not "") and (is_on_sale is not False)):
      is_on_sale = True
    else:
      is_on_sale = False
      
    self.name = name
    self.image = image
    self.price = price.replace("$","").strip()
    self.unit = unit
    self.is_on_sale = is_on_sale
    self.product_comparison_price = product_comparison_price.replace("$","").strip()
    self.product_comparison_unit = product_comparison_unit.replace("/","").strip()
    self.product = product
    self.brand = brand
    self.locked = False
    self.updated = updated

  def exportJSON(self):
    return {
      'name': self.name,
      'image': self.image,
      'price': float(self.price) if self.price is not "" else 0,
      'unit': self.unit,
      'onSale': self.is_on_sale,
      "comparisonPrice": float(self.product_comparison_price) if self.product_comparison_price is not "" else self.product_comparison_price,
      "comparisonUnit": self.product_comparison_unit,
      "locked": self.locked,
      "brand": self.brand,
      "updated": self.updated,
      "product": self.product,
      "createdAt": datetime.now()
    }

  def getName(self):
    return self.name

  def getUpdated(self):
    return self.updated

  def setProduct(self, product=""):
    self.product = product

  def setBrand(self, brand=""):
    self.brand = brand

  def setLocked(self, locked=False):
    self.locked = locked

  def setUpdated(self, update=False):
    self.updated = update
