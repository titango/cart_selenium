
from selenium.webdriver.common.by import By

class Locators():
    # --- Home Page Locators ---
    SEARCH_TEXTBOX=(By.ID, "search-input__input")
    
    #Product Search Page
    PRODUCT_TILE_GROUP_LIST = (By.CLASS_NAME,"product-tile-group__list")
    PRODUCT_NAME = (By.CLASS_NAME, "product-name__item--name")
    PRODUCT_PRICE = (By.CLASS_NAME, "price__value")
    PRODUCT_UNIT = (By.CLASS_NAME, "price__unit")
    PRODUCT_IS_ON_SALE = (By.CLASS_NAME, "product-badge__icon__text--sale")
    PRODUCT_COMPARISON_PRICE = (By.CLASS_NAME, "comparison-price-list__item__price__value")
    PRODUCT_COMPARISON_UNIT = (By.CLASS_NAME, "comparison-price-list__item__price__unit")