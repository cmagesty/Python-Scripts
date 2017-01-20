import time
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

emails = ['k@lacesociety.com', 'l@lacesociety.com', 'm@lacesociety.com', 'n@lacesociety.com', 'o@lacesociety.com', 'p@lacesociety.com', 'q@lacesociety.com', 'r@lacesociety.com', 's@lacesociety.com', 't@lacesociety.com', 'u@lacesociety.com', 'v@lacesociety.com']
print("[" + strftime("%I:%M:%S") + "]" + " Start LSendRaffles.py")
for x in emails :

    i = 1

    browser = webdriver.Chrome('//Users//Chris//Desktop//chromedriver')
    browser.get('https://launches.endclothing.com/#/products/211/')
    time.sleep(1)

    emailElem = browser.find_element_by_name('email')
    emailElem.send_keys(x)
    emailElem.submit()
    time.sleep(1)

    #firstNameElem = browser.find_element_by_name('firstName')
    #firstNameElem.send_keys('Chris')

    #lastNameElem = browser.find_element_by_name('lastName')
    #lastNameElem.send_keys('Magesty')

    passElem = browser.find_element_by_name('password')
    passElem.send_keys('bilabong11')
    passElem.submit()
    time.sleep(3)

#--------------------------END FIRST PAGE-----------------------------------------

    select = Select(browser.find_element_by_name('size'))
    select.select_by_visible_text('UK 9')

    #select.select_element_by_value('CONTINUE').click()
    browser.find_element_by_xpath(".//*[@id='register']/div[2]/input").click()
    time.sleep(5)
# --------------------------End Second Page----------------------------------------

    fNBElem = browser.find_element_by_name('firstNameBlock')
    fNBElem.send_keys('Chris')

    lNBElem = browser.find_element_by_name('lastNameBlock')
    lNBElem.send_keys('Magesty')

    telephoneElem = browser.find_element_by_name('telephoneBlock')
    telephoneElem.send_keys('5516970672')

    fNBElem = browser.find_element_by_name('addressLine1Block')
    fNBElem.send_keys('64 Grand Pl')

    lNBElem = browser.find_element_by_name('townCityBlock')
    lNBElem.send_keys('Kearny')

    select = Select(browser.find_element_by_name('regionBlock'))
    #select by visible text
    select.select_by_visible_text('New Jersey')

    telephoneElem = browser.find_element_by_name('postcodeBlock')
    telephoneElem.send_keys('07032')
    telephoneElem.submit()
    time.sleep(5)
# --------------------------End Third Page----------------------------------------
    time.sleep(5)
    fNBElem = browser.find_element_by_name('cardNumber')
    fNBElem.send_keys('371249493001006')

    selectMonth = browser.find_element_by_xpath(".//*[@id='payment-options']/div[2]/div[2]/div[1]/div/select/option[text()='Aug']").click()
    #selectMonth.select_by_value('8')

    selectYear = browser.find_element_by_xpath(".//*[@id='payment-options']/div[2]/div[2]/div[2]/div/div/select/option[text()='2020']").click()
    #selectYear.select_by_visible_text(2020)

    telephoneElem = browser.find_element_by_name('securityCode')
    telephoneElem.send_keys('6854')

    browser.find_element_by_xpath(".//*[@id='register']/div/form/label/div").click()
    browser.find_element_by_xpath(".//*[@id='register']/div/form/div[3]/div/input").click()
    time.sleep(6)
    browser.close()

print("[" + strftime("%I:%M:%S") + "]" + "End Script")