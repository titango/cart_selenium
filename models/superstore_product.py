# PYTHON MODEL FOR SUPERSTORE PRODUCT
from datetime import datetime

class SuperStoreProduct():
  def __init__(self, name, price, unit, is_on_sale, product_comparison_price, product_comparison_unit):
    if(is_on_sale is not ""):
      is_on_sale = True
    else:
      is_on_sale = False
      
    self.name = name
    self.price = price
    self.unit = unit
    self.is_on_sale = is_on_sale
    self.product_comparison_price = product_comparison_price
    self.product_comparison_unit = product_comparison_unit.replace("/","").strip()

  def exportJSON(self):
    return {
      'name': self.name,
      'price': self.price,
      'unit': self.unit,
      'onSale': self.is_on_sale,
      "comparisonPrice": self.product_comparison_price,
      "comparisonUnit": self.product_comparison_unit,
      "date": datetime.now()
    }
