from selenium import webdriver
'''This is a basic test for using selenium 
Step:
1. Go to google.com
2. type in test, and submit the result
3.  scrrenshot the result
4. close browser

chenchih 20200328
'''
import time
def setup():
    global browser
    browser=webdriver.Chrome('D:\\chromedriver.exe')
    browser.maximize_window()
def test_accessurl():
    ####user enter their url##############
    #url=input("please enter your url: ")
    #browser.get(url)
    #######google's textbar id class name#######
    browser.get('https://www.google.com')
    element= browser.find_element_by_class_name('gLFyf.gsfi')
    element.send_keys('test')    
    element.submit() 
    #######yahoo's textbar id class name#######
    #browser.get('https://tw.yahoo.com/')
    #element=browser.find_element_by_id('header-search-input')
def teardown():
    browser.implicitly_wait(5)
    browser.save_screenshot('google_result.png')    
    browser.close()
    browser.quit()

setup()
test_accessurl()
teardown()


