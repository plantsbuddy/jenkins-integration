from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to Google's home page
driver.get("https://www.google.com")

# Find the Google logo element by class name
logo = driver.find_element_by_class_name("lnXdpd")

# Verify if the Google logo is displayed
assert logo.is_displayed(), "Google logo is not displayed on the page."

# Print a success message if the assertion passes
print("Test passed! Google logo is displayed on the page.")

# Close the browser
driver.quit()
