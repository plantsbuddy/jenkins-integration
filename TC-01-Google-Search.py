from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to Google's home page
driver.get("https://www.google.com")

# Find the search input element and enter a search query
search_input = driver.find_element_by_name("q")
search_input.send_keys("selenium")
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(3)

# Verify the page title of the search results page
expected_title = "selenium - Google Search"
actual_title = driver.title
assert expected_title == actual_title, f"Page title does not match. Expected: '{expected_title}', Actual: '{actual_title}'"

# Print a success message if the assertion passes
print("Test passed! Google search for 'selenium' returned the expected results.")

# Close the browser
driver.quit()
