from selenium import webdriver
import pandas

PATH = "/Users/matthewyekell/Downloads/chromedriver"
# chromedriver download link: https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome(PATH)

driver.get("https://www.switchbackr.com/l/5fad1bf8-491a-4dc5-b80d-f774850d57f8")

listing_titles = []
retail_prices = []
discount_rates = []

main = driver.find_element_by_id('root')
listing_title = main.find_element_by_class_name("ListingPage_modelTitle__aRRis").text
sale_price = main.find_element_by_class_name("ListingPage_priceTitle__2-Hbn").text
discount_rate = main.find_element_by_class_name("ListingPage_discountPercentage__1GLcS").text

discount = discount_rate[:-4]

print(listing_title, sale_price, discount)