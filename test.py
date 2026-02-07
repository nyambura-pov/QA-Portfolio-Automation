from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 1. Initialize the Chrome Driver (Opens the browser)
driver = webdriver.Chrome()

# 2. Navigate to a website
driver.get("https://www.google.com")

# 3. Find the search bar using its 'name' attribute
search_bar = driver.find_element("name", "q")

# 4. Type and press Enter
search_bar.send_keys("Selenium Python Automation" + Keys.RETURN)

# 5. Wait 2 seconds to see the result, then close
time.sleep(2)
print("Page Title is:", driver.title)
driver.quit()