import time
from playwright.sync_api import sync_playwright

# Start Playwright
with sync_playwright() as p:
    # Launch the browser in edge:
    edge_executable_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
    browser = p.chromium.launch(headless=False)  # Set headless=True to run without a UI

    # Open a new page
    page = browser.new_page()

    # Navigate to the specified URL
    page.goto("https://alstom-sso.prd.mykronos.com/wfd/home?tenantId=alstom_prd_01")

    #Wait for page to load fully
    page.wait_for_load_state("networkidle")

    time.sleep(20)


# This waits for the link/button
        #//*[@id="myAccrualsTile"] ,, //*[@id="myAccrualsTile"]/krn-ng-screen-reader-only/span
    page.wait_for_selector('//*[@id="myAccrualsTile"]')
    

    
    # Wait for the "Accurals" link to be visible and click it
    page.click('//*[contains(text(),"Apply Leaves, OD, WFH etc")]')
    
    # Makes page load fully
    page.wait_for_load_state("networkidle")
    


    # Optional: wait a bit to see the result of the click
    page.wait_for_timeout(1000)
    
    # Wait for 2 seconds
    time.sleep(20)

    # This waits for the link/button and selects/identifies
        #//*[@id="myAccrualsTile"] ,, //*[@id="myAccrualsTile"]/krn-ng-screen-reader-only/span
    page.wait_for_selector('//*[@id="myAccrualsTile"]')
    

     # Wait for the "Accurals" link to be visible and click it
    page.click('//*[@title="IND-Work From Home-MEP")]')
    # Clicking the link to access the tile on the page


    page.wait_for_load_state("networkidle")
   

      # Optional: wait a bit to see the result of the click
    page.wait_for_timeout(1000) 


    # This waits for the link/button and selects/identifies WFH Button ID
    page.wait_for_selector('//*[@title="IND-Work From Home-MEP"]')

     # Wait for the "WFH" link to be visible and click it
    page.click('//*[@title="IND-Work From Home-MEP")]')  
    page.wait_for_load_state("networkidle")
    


    # Optional: wait a bit to see the result of the click
    page.wait_for_timeout(2000)  # Wait for 2 seconds
    #time.sleep(20)

    # Close the browser
    #browser.close()