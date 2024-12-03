import time
from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch a Chromium browser
    browser = playwright.chromium.launch(headless=False)  # Set headless=True to run without UI
    page = browser.new_page()

    # Navigate to the target website
    page.goto("https://webpack.github.io/shadow-dom/")

    #Wait for page to load fully
    page.wait_for_load_state("networkidle")

    time.sleep(20)

    # Access the shadow host element using its selector
    shadow_host = page.query_selector('my-element')

    if shadow_host:
        # Access the shadow root of the shadow host
        shadow_root = shadow_host.evaluate_handle('el => el.shadowRoot')

        # Query the desired button element inside the shadow DOM (replace with the actual selector)
        shadow_button = shadow_root.query_selector('button')

        if shadow_button:
            shadow_button.click()  # Click on the button inside the shadow DOM
            print("Clicked the button within the shadow element.")
        else:
            print("Button inside the shadow DOM not found.")
    else:
        print("Shadow host not found.")

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)