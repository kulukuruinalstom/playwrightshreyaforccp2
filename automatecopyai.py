from playwright.sync_api import sync_playwright

# Start Playwright
with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)  # Set headless=True to run without a UI
    # Open a new page
    page = browser.new_page()

    # Navigate to the specified URL
    page.goto("https://the-internet.herokuapp.com/")

    # Wait for the "Basic Auth" link to be visible and click it
    page.click("text='Basic Auth'")  # Clicking the link to access the Basic Auth page

    # Wait for the button to be visible (the button should be the link "Go to the secure area")
    page.wait_for_selector("a[href='/basic_auth']")  # This waits for the link/button

    # Click the button (link) to go to the secured area
    page.click("a[href='/basic_auth']")  # Clicking the secured area link

    # Optional: wait a bit to see the result of the click
    page.wait_for_timeout(2000)  # Wait for 2 seconds

    # Close the browser
    browser.close()