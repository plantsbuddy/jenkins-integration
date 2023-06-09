from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to Google's home page
driver.get("https://www.google.com")

# Find the Gmail link
gmail_link = driver.find_element_by_link_text("Gmail")

# Click on the Gmail link
gmail_link.click()

# Wait for the page to load
driver.implicitly_wait(3)

# Get the title of the current page
current_title = driver.title

# Validate if the title contains "Gmail"
assert "Gmail" in current_title, "Page title does not contain 'Gmail' after clicking the Gmail link."

# Print a success message if the assertion passes
print("Test passed! Clicked on the Gmail link and the page title changed to reflect Gmail.")

# Close the browser
driver.quit()
