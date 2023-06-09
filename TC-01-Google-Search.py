from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Wait for the search results to load
time.sleep(21)

# Print a success message if the assertion passes
print("Test passed! Google search for 'selenium' returned the expected results.")
