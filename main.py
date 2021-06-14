# Main executable file
from scripts import product_scraping_script
from models.product import Product
from lib.saveonfood import SaveOnFoodPage
from lib.superstore import SuperStorePage

def main():
  print("Staring program in main.py")
  
  # Run superstore script
  product_scraping_script.run(Product, SuperStorePage, "superstore")

  # Run saveonfood script
  product_scraping_script.run(Product, SaveOnFoodPage, "saveonfood")

if __name__ == "__main__":
  main()