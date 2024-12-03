from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch a Chromium browser
    browser = playwright.chromium.launch(headless=False)  # Set headless=True if you don't want to see the browser
    page = browser.new_page()

    # Navigate to the target website
    page.goto("https://practice.expandtesting.com/shadowdom")  

    #Wait for page to load fully
    page.wait_for_load_state("networkidle")

    #playwright codegen https://practice.expandtesting.com/shadowdom

    # Access the shadow host element (replace '.shadow-host' with the actual selector)
    shadow_host = page.query_selector('#my-btn')

    # Access the shadow root
    shadow_root = shadow_host.evaluate_handle('el => el.shadowRoot')

    # Query an element inside the shadow DOM (replace '.shadow-element' with the actual selector)
    shadow_element = shadow_root.query_selector('.shadow-element')
    
    if shadow_element:
        shadow_element.click()  # Click on the shadow element
        print("Clicked on the shadow element.")
    else:
        print("Shadow element not found.")

    # Close the browser
    #browser.close()

with sync_playwright() as playwright:
    run(playwright)