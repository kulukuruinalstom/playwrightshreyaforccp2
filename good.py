import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")
    time.sleep(50)
    page.get_by_placeholder("Enter pizza name").click()
    #page.get_by_placeholder("Enter pizza name").click()
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
