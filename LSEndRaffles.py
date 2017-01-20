import time
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

emails = [ ]
print("[" + strftime("%I:%M:%S") + "]" + " Start LSendRaffles.py")
for x in emails :
    
    browser = webdriver.Chrome('//Users//Chris//Desktop//chromedriver')
    browser.get('https://launches.endclothing.com/#/products/211/')
    time.sleep(1)

    emailElem = browser.find_element_by_name('email')
    emailElem.send_keys(x)
    emailElem.submit()
    time.sleep(1)
    
    passElem = browser.find_element_by_name('password')
    passElem.send_keys(' ')
    passElem.submit()
    time.sleep(3)

#--------------------------END FIRST PAGE-----------------------------------------

    select = Select(browser.find_element_by_name('size'))
    select.select_by_visible_text(' ')
    
    browser.find_element_by_xpath(".//*[@id='register']/div[2]/input").click()
    time.sleep(5)
# --------------------------End Second Page----------------------------------------

    fNBElem = browser.find_element_by_name('firstNameBlock')
    fNBElem.send_keys('')

    lNBElem = browser.find_element_by_name('lastNameBlock')
    lNBElem.send_keys('')

    telephoneElem = browser.find_element_by_name('telephoneBlock')
    telephoneElem.send_keys(' ')

    adElem = browser.find_element_by_name('addressLine1Block')
    adElem.send_keys(' ')

    cityElem = browser.find_element_by_name('townCityBlock')
    cityElem.send_keys(' ')

    select = Select(browser.find_element_by_name('regionBlock'))
    #select by visible text
    select.select_by_visible_text(' ')

    codeElem = browser.find_element_by_name('postcodeBlock')
    codeElem.send_keys(' ')
    codeElem.submit()
    time.sleep(5)
# --------------------------End Third Page----------------------------------------
    time.sleep(5)
    cnElem = browser.find_element_by_name('cardNumber')
    cnElem.send_keys(' ')

    selectMonth = browser.find_element_by_xpath(".//*[@id='payment-options']/div[2]/div[2]/div[1]/div/select/option[text()='Aug']").click()
 
    selectYear = browser.find_element_by_xpath(".//*[@id='payment-options']/div[2]/div[2]/div[2]/div/div/select/option[text()='2020']").click()

    scElem = browser.find_element_by_name('securityCode')
    scElem.send_keys(' ')

    browser.find_element_by_xpath(".//*[@id='register']/div/form/label/div").click()
    browser.find_element_by_xpath(".//*[@id='register']/div/form/div[3]/div/input").click()
    time.sleep(6)
    browser.close()

print("[" + strftime("%I:%M:%S") + "]" + "End Script")
