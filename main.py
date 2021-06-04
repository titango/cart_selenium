# Main executable file
from scripts import product_scraping_script
from models.saveonfood_product import SaveOnFoodProduct
from models.superstore_product import SuperStoreProduct
from lib.saveonfood import SaveOnFoodPage
from lib.superstore import SuperStorePage

def main():
  print("Staring program in main.py")
  
  # Run superstore script
  # product_scraping_script.run(SuperStoreProduct, SuperStorePage, "superstore", 10)

  # Run saveonfood script
  product_scraping_script.run(SaveOnFoodProduct, SaveOnFoodPage, "saveonfood", 1)

if __name__ == "__main__":
  main()