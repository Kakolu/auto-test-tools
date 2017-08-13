import time
from splinter import Browser


with Browser(‘chrome’) as browser:
    # Visit URL
    url = “”
    browser.visit(url)
    #time.sleep(5)
    browser.visit(url)
    browser.fill(‘companyId’, ‘’)
    browser.fill(‘j_username’, ‘’)
    browser.fill(‘j_password’, ‘’)
    # Find and click the ‘search’ button
    button = browser.find_by_id(‘login’)
    # Interact with elements
    button.click()
    if browser.is_text_present(‘Phoenix’):
        print(“Yes, you have successfully logged in!“)
    else:
        print(“No, login unsuccessful”)
    time.sleep(5)