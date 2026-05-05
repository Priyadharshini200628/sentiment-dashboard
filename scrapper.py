from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com")

time.sleep(3)

quotes = driver.find_elements(By.CLASS_NAME, "text")

data = []

for q in quotes:
    data.append(q.text)

# Save in same folder as your code
file_path = os.path.join(os.getcwd(), "reviews.txt")

with open(file_path, "w", encoding="utf-8") as f:
    for item in data:
        f.write(item + "\n")

print("Data saved successfully at:", file_path)

driver.quit()