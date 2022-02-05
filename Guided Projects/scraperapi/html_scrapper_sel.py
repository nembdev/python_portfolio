import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver import Firefox

# starting page to scrape
page_number = 1
url = f"https://www.g2.com/search?button=&page={page_number}&query=salesforce"
# print(url)

# start the browser
driver = Firefox()

# open the url
# driver.get(url)

# save the source code to a file
# with open(file, mode) as file_object
# with open("scripts/test.html", "w") as file:
#    file.write(driver.page_source)


for page in range(1, 64):
    url = f"https://www.g2.com/search?button=&page={page_number}&query=salesforce"
    driver.get(url)

    # wait to load
    time.sleep(5)

    with open(f"scripts/test_{page}.html" "w") as file:
        file.write(driver.page_source)

    page_number += 1
