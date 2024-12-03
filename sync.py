import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://alstom-sso.prd.mykronos.com/wfd/home")
    time.sleep(30)

    page.screenshot(path="demo.png")

    time.sleep(30)

    browser.close()