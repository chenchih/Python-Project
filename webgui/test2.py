import weblogin
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys


def StopTest(msg):
    print (msg)
    #weblogin.driver.quit()
    weblogin.driver.quit()
    sys.exit()
    

try:
    #WebDriverWait(weblogin.driver, 60).until(EC.title_contains("CGNV4-EU Login - Hitron Technologies"))
    WebDriverWait(weblogin.driver, 10).until(EC.title_contains("Google"))
    print("Page title is: %s" %(weblogin.driver.title))
except:
    StopTest("Connect Fail")
'''
try:
    weblogin.driver.find_element_by_id("login_username").clear()
    weblogin.driver.find_element_by_id("login_username").send_keys(weblogin.account)
    weblogin.driver.find_element_by_id("login_password").clear()
    weblogin.driver.find_element_by_id("login_password").send_keys(weblogin.password)
    weblogin.driver.find_element_by_id("Button_Login").click()
except:
    StopTest("Exception")

try:
    WebDriverWait(weblogin.driver, 30).until(EC.title_contains("CGNV4-EU Router - Hitron Technologies"))
except:
    StopTest("Login Fail")

print ("Login Ok")

# Logout
try:
    element = WebDriverWait(weblogin.driver, 30).until(
        EC.element_to_be_clickable((By.ID, "currentUser"))
    )
    element.click()
    
    element = WebDriverWait(weblogin.driver, 30).until(
        EC.element_to_be_clickable((By.ID, "btnLogout"))
    )
    element.click()

    WebDriverWait(weblogin.driver, 30).until(EC.title_contains("CGNV4-EU Login - Hitron Technologies"))
except:
    StopTest("Logout Fail") '''


time.sleep(1)
#weblogin.driver.quit()
weblogin.driver.quit()






