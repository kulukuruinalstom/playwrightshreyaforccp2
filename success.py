import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/shadowdom")
    page.get_by_role("button", name="This button is inside a").click()
    time.sleep(2000)
    
    # ---------------------
    context.close()
    browser.close()



with sync_playwright() as playwright:
    run(playwright)
