"""
Title:Custom insta unfollow bot [Python tutorial]
Link: https://www.youtube.com/watch?v=58w8lXRnJ3Q
Youtuber/author: Max Codez
status: Done PASS
"""
from selenium import webdriver
from time import sleep
driverPath = 'D:\\test\\chromedriver.exe'
driver = webdriver.Chrome(driverPath)
driver.get("https://instagram.com")
sleep (4)
user = "username"
pwd = "password"
driver.find_element_by_xpath("//input[@name=\"username\"]")\
                        .send_keys(user)
driver.find_element_by_xpath("//input[@name=\"password\"]")\
                        .send_keys(pwd)
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(4)

#driver.get("https://instagram.com/MaxCodez_")
#Access to your page
driver.get("https://www.instagram.com/chenchih.test")
#click not now
#driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
'''
if your instgram some are english some are chinese, you can used these method for multiply string:

#for i in range(3):
method1 - type correect string, but only one at a time, you decide to use chinese or english
#following = driver.find_element_by_partial_link_text("following").click()
#following = driver.find_element_by_partial_link_text("追蹤中").click()
method 2: using try or except method
try:
    following = driver.find_element_by_partial_link_text('following').click() 
except:
    driver.find_element_by_partial_link_text('追蹤中').click()
  
method 3 used the class will select 
driver.find_elements_by_xpath("//span[contains(@class,'g47SY')]")[2].text)

method 4 the best method
driver.find_element_by_xpath("//*[text()[contains(.,'following') or contains(.,'追蹤中')]]  ").click()   

sleep(5)
'''

sleep(2)
for i in range(1):
    driver.find_element_by_xpath("//*[text()[contains(.,'following') or contains(.,'追蹤中')]]  ").click() 
    #driver.find_element_by_xpath('//button[text()= "Following"]').click()
    #driver.find_element_by_xpath('//button[text()= "Unfollow"]').click()
    #driver.find_element_by_xpath('//button[text()= "追蹤"]').click()
    sleep(2)
    driver.find_element_by_xpath('//button[text()= "追蹤中" or text()= "Following"]').click()
    driver.find_element_by_xpath('//button[text()= "取消追蹤" or text()= "Unfollow"]').click()
    sleep(3)
    
    
#driver.refresh()
