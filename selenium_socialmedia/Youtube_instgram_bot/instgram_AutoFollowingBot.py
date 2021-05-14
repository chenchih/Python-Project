"""
Title:Custom How to build an autofollow bot for instagram!
Link: https://www.youtube.com/watch?v=el1b7AgsShw&t=125s
Youtuber/author: Max Codez
status: PASS
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
#click not now
for i in range(2):
    driver.find_element_by_xpath("//button[contains(text(), '稍後再說')]").click()
sleep(3)
#for i in ranve(3):
#open See all follower
#driver.find_element_by_xpath("//div[contains(text(),\"See All\")]").click()
driver.find_element_by_xpath("//div[contains(text(),\"查看全部\")]").click()

for i in range(1):
    #driver.find_element_by_xpath('//button[text()= "Follow"]').click()
    driver.find_element_by_xpath('//button[text()= "追蹤"]').click()
#driver.refresh()
