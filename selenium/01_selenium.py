from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



def main():
    global driver
    website = 'https://www.adamchoi.co.uk/overs/detailed'
    service = Service('/Users/itsyuimoriispace/Downloads/chromedriver_mac64/chromedriver')
    # define 'driver' variable
    driver = webdriver.Chrome(service=service)
    # open Google Chrome with chromedriver
    driver.get(website)

    # locate and click on a button

    all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
    all_matches_button.click()

    elements = driver.find_elements(By.TAG_NAME, 'tr')
    for element in elements:
        # Process each matching element
        print(element.text)
    # driver.quit()

if __name__ == '__main__':
    main()