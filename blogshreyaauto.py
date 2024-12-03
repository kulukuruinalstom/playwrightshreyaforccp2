import time
from playwright.sync_api import sync_playwright
# Start Playwright
with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)  # Set headless=True to run without a UI
    # Open a new page
    page = browser.new_page()
    # Navigate to the specified URL
    page.goto("https://shreyakulukuru.wordpress.com/about/")
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    page.wait_for_selector('//*[@id="menu-primary-1"]/li[2]/a')
   # Wait for the "Blog" link to be visible and click it
    page.click('//*[@id="menu-primary-1"]/li[2]/a')
    # Wait for the button to be visible (the button should be the link "Go to the secure area")
    # Click the button (link) to go to the secured area
    #page.click("text='Blog'")  # Clicking the secured area link
    # Optional: wait a bit to see the result of the click
    #page.wait_for_timeout(2000)  # Wait for 2 seconds
    time.sleep(20)
    # Close the browser
    #browser.close()