from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''This is a basic test for using selenium 
Step:
1. Go to amazon.com
2. type in dress, and enter
3.  check thre result is dress or not
4. close browser

chenchih 20200328
'''
import time
def setup():  
    global browser
    browser=webdriver.Chrome('D:\\chromedriver.exe')
    browser.maximize_window()
    browser.implicitly_wait(5) 
def test_accessurl():
    browser.get('https://www.amazon.com')
    #element= browser.find_element_by_id('twotabsearchtextbox')
    search = browser.find_element(By.ID,'twotabsearchtextbox')
    search.send_keys('dress', Keys.ENTER)    
    #expected_text = '"dress"'
    #actual_text = browser.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    #assert expected_text == actual_text, f'Error, Expected text: {expected_text}, but actual text: {actual_text}'
    #search.submit() 
def check_result():
    expected_text = '"dress"'
    actual_text = browser.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    #print(actual_text)
    assert expected_text == actual_text, f'Error, Expected text: {expected_text}, but actual text: {actual_text}'
def teardown():
    browser.implicitly_wait(5)
    browser.save_screenshot('result.png')    
    browser.close()
    browser.quit()

setup()
test_accessurl()
check_result()
teardown()


