
from selenium.webdriver.common.by import By

class Locators():
    # --- Home Page Locators ---
    SEARCH_TEXTBOX=(By.CLASS_NAME, "InputField-sc-134vw7x")
    
    #Product Search Page
    PRODUCT_TILE_GROUP_LIST = (By.CLASS_NAME,"Content-sc-ite0cu")
    PRODUCT_TRACKING = (By.CLASS_NAME, "ColListing-sc-lcurnl")
    PRODUCT_NAME = (By.CLASS_NAME, "ProductCardTitle-sc-ye20s3")
    PRODUCT_IMAGE = (By.CLASS_NAME, "Image-sc-1dk4b58")
    PRODUCT_PRICE = (By.CLASS_NAME, "ProductCardPrice-sc-zgh1l1")
    # PRODUCT_UNIT = (By.CLASS_NAME, "price__unit") - DOES NOT HAVE
    # PRODUCT_IS_ON_SALE = (By.CLASS_NAME, "product-badge__icon__text--sale")
    PRODUCT_COMPARISON_PRICE = (By.CLASS_NAME, "ProductCardPriceInfo-sc-1o21dmb")
    # PRODUCT_COMPARISON_UNIT = (By.CLASS_NAME, "comparison-price-list__item__price__unit")