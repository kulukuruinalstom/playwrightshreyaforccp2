import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://shreyakulukuru.wordpress.com/about/")

    page.wait_for_load_state("networkidle")
    page.wait_for_selector("text=Blog")
    #page.wait_for_selector("button Blog")

    #page.screenshot(path="demo.png")

    page.click("text=blog")

    page.wait_for_load_state("networkidle")

    page.screenshot(path="demo.png")

    #time.sleep(30)

    browser.close()
    