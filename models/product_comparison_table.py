# PYTHON MODEL FOR SUPERSTORE PRODUCT
from datetime import datetime

class ComparisonTable():
  def __init__(self, product, store_product):
    self.product = product
    self.store_product = store_product

  def exportJSON(self):
    return {
      'product': self.product,
      'store_product': [self.store_product],
      'createdAt': datetime.now()
    }
