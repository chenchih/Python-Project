from selenium import webdriver
import time
def setup():
    global browser
    browser=webdriver.Chrome('D:\\chromedriver.exe')
    browser.maximize_window()
def test_accessurl():
    browser.get('https://tw.yahoo.com/')
    #browser.find_element_by_class_name('gLFyf.gsfi').send_keys('test')
    element=browser.find_element_by_id('header-search-input')
    element.send_keys('test')
    element.submit() 
def teardown():
    browser.implicitly_wait(5)
    browser.save_screenshot('result.png')    
    browser.close()
    browser.quit()

setup()
test_accessurl()
teardown()




#
