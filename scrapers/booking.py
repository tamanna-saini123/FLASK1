from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrap_booking_data():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.booking.com/")
    time.sleep(3)

    search = driver.find_element(By.NAME, "ss")
    search.send_keys("Delhi")
    search.send_keys(Keys.ENTER)

    time.sleep(8)

    hotels = driver.find_elements(
        By.CSS_SELECTOR,
        'div[data-testid="property-card"]'
    )

    data = []

    for hotel in hotels:

        try:
            name = hotel.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="title"]'
            ).text
        except:
            name = "N/A"

        try:
            rating = hotel.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="review-score"]'
            ).text
        except:
            rating = "N/A"

        try:
            link = hotel.find_element(
                By.TAG_NAME,
                "a"
            ).get_attribute("href")
        except:
            link = "N/A"

        try:
            image = hotel.find_element(
                By.TAG_NAME,
                "img"
            ).get_attribute("src")
        except:
            image = ""

        data.append({
            "Hotel Name": name,
            "Rating": rating,
            "Hotel Link": link,
            "Image URL": image
        })

    driver.quit()

    return data