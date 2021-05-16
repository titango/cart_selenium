# Main executable file
from lib.superstore import SuperStorePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
  print("Staring program in main")
  
  # Driver from chrome
  driver = webdriver.Chrome()

  sp = SuperStorePage(driver)
  
  # pageSource = driver.page_source

  try: 
    # Search for search bar

    sp.search("apple")
    product_list = sp.getAlSearchedlProducts()
    print(product_list)
    # div_thumbnail = li.find_element_by_class_name("product-tile__thumbnail__image")
    # product_image = WebDriverWait(div_thumbnail, 10).until(
    #   EC.presence_of_element_located((By.CLASS_NAME, "responsive_image"))
    # )
    # print("div_image: ", product_image.get_attribute("src"))
    
  except Exception as e:
    print(e)
    driver.quit()

  # End the browser
  driver.quit()

if __name__ == "__main__":
  main()