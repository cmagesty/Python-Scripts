import time
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

print '''
##########################################################################################################
#                                                                                                        #
#     ##        ###    ######## ########   ######## ######## ######## ## ######## ######## ##    ##      #
#     ##       ## ##   ##       ##         ##       ##    ## ##       ## ##          ##    ###  ###      #
#     ##      ##   ##  ##       ##         ##       ##    ## ##       ## ##          ##     ##  ##       #
#     ##     ##     ## ##       #####      ######## ##    ## ##       ## #####       ##     ######       #
#     ##     ######### ##       ##               ## ##    ## ##       ## ##          ##       ##         #
#     ##     ##     ## ##       ##               ## ##    ## ##       ## ##          ##       ##         #
#     ###### ##     ## ######## ########   ######## ######## ######## ## ########    ##       ##         #
#                                                                                                        #
################## by @ChrisMagesty; remove alerts@lacesociety.com from spam folder;######################
       '''
print("[" + strftime("%I:%M:%S") + "]" + " Start emails.py")

browser = webdriver.Chrome('//Users//Chris//Desktop//chromedriver')
browser.get('') #enter cpanel login url for website
time.sleep(5)
print("[" + strftime("%I:%M:%S") + "]" + "Open New Browser")

lastNameElem = browser.find_element_by_id('user')
lastNameElem.send_keys('user')
print("[" + strftime("%I:%M:%S") + "]" + "login")

emailElem = browser.find_element_by_id('pass')
emailElem.send_keys(' pass')
print("[" + strftime("%I:%M:%S") + "]" + "password")
emailElem.submit()
time.sleep(5)
element = browser.find_element_by_xpath(".//*[@id='item_accounts']")
element.click()

emails = [] #put email names to make in arry
for x in emails:
    addemailElem = browser.find_element_by_id('add_email_account')
    addemailElem.send_keys(x)
    print("[" + strftime("%I:%M:%S") + "]" + "email added" + x)

    lastNameElem = browser.find_element_by_id('add_email_password1')
    lastNameElem.send_keys('password')
    print("[" + strftime("%I:%M:%S") + "]" + "pass added")

    emailElem = browser.find_element_by_id('add_email_password2')
    emailElem.send_keys('password')
    print("[" + strftime("%I:%M:%S") + "]" + "password2 added")

    element = browser.find_element_by_xpath(".// *[ @ id = 'add_email_create']")
    element.click()

    print("[" + strftime("%I:%M:%S") + "]" + "email created")
    time.sleep(3)

print("[" + strftime("%I:%M:%S") + "]" + "End Script")
