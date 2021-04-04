from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from account import FBusername, FBpassword
PATH = 'D:\\chromedriver.exe'
##### Handling of Allow Pop Up In Facebook
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

#browser=webdriver.Chrome('D:\\chromedriver.exe')
#browser.get('https://www.facebok.com/')

browser = webdriver.Chrome(chrome_options=option, executable_path=PATH)
browser.maximize_window()

def loginFB(id,password):
    browser.get("https://www.facebook.com/")

    # store the credentials
    #user_id=FBusername
    #password=FBpassword

    #user input
    user_id=input('Enter Your Username:')
    password=getpass('Enter Password:')

    # find the email input and send the email or phone credential
    user_box = browser.find_element_by_id("email")  # For detecting the user id box
    user_box.send_keys(user_id)                     # Enter the user id in the box

    # send the password
    password_box = browser.find_element_by_id("pass")   # For detecting the password box
    password_box.send_keys(password)                    # For detecting the password in the box

    # click the login
    login_box = browser.find_element_by_name("login")  # For detecting the Login button
    login_box.click()
    #print(f"Login succes, welcome{user_id}, 5 second will quit")

loginFB("YOUR_FACEBOOK_ID","YOUR_FACEBOOK_PASSWORD") 
sleep(5)    
browser.close()
browser.quit()
