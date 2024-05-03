# you_tube_scraper.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()  # You can use other browsers too
driver.set_page_load_timeout(10)
driver.get('https://www.youtube.com/')  # Replace with the YouTube video URL
driver.maximize_window()
sleep(5)

# Find the search input field and interact with it
search = driver.find_element(By.NAME, "search_query")
# Perform further actions as needed (e.g., search for a video, navigate to comments section, etc.)
