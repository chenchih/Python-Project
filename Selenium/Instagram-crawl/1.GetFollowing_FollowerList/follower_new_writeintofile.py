'''
https://www.youtube.com/watch?v=d2GBO_QjRlo
'''
from selenium import webdriver
from time import sleep
from getpass import getpass
from datetime import datetime
option = webdriver.ChromeOptions()
option.add_argument('--lang=en-US')
option.add_argument('--window-size=1200,1000')
line = "#"*15
#time and datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)
class InstaBot:
    def __init__(self,username,password):
        #assign username to self so that other method can used it 
        self.username=username
        #self.password=password
        #driverPath = 'D:\\chromedriver.exe'
        driverPath = 'C:\\webdriver\\chromedriver.exe'
        self.browser=webdriver.Chrome(driverPath,chrome_options=option)
        self.browser.get("http://instagram.com")
        sleep(2)
        #go into signup page
        #self.driver.find_element_by_xpath("//span[contains(text(),'Sign')]").click()
        # find the email input and send the email or phone credential
        #user_box = self.browser.find_element_by_name("username")  # For detecting the user id box
        #user_box.send_keys(username)
        self.browser.find_element_by_name("username").send_keys(username) # Enter the user id in the box
        # send the password
        password_box = self.browser.find_element_by_name("password")   # For detecting the password box
        password_box.send_keys(password)                    # For detecting the password in the boxs
        #login
        #login_box = self.browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]')[0]
        self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        #print(f"{line} Login In Success!!! {line}")
        #Skip notification
        sleep(3)
        self.browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(2)
        self.browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(2)
        #go to profile page
        self.browser.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
        sleep(2)
    # convert list to string
    def converting (self, nameList):
        IGuserName = "\n".join(nameList)
        return IGuserName
    def following_user(self):
        #click on following button(People you are following; people you like)
        self.browser.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        sleep(2)
        # copy the xpath of scrollbar
        # scroll_box = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
        scroll_box = self.browser.find_element_by_xpath("//div[@class='isgrP']")
        sleep(3)
        # height variable
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            # scroll down and retrun the hight of scroll
            ht = self.browser.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)
        # list follower name
        sleep(5)
        #print(f"{line} Scroll Buttom  Done!!! {line}")
        links = scroll_box.find_elements_by_tag_name('a')
        sleep(2)
        names = [name.text for name in links if name.text != '']
        #print(f"{line} follower list done!!! {line}")
        # hit close button
        #notworking
        #self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
        return names

    def follower_user(self):
        #clik on follower (people who follow you)
        self.browser.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
        #print(f"{line} Follower  Done!!! {line}")
        sleep(4)
        # scrollbar xpath
        #notworking
        #scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/ul/div")
        scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
        # scroll_box= self.browser.find_element_by_xpath("//div[@class='PZuss']")
        # scroll_box=self.browser.find_element_by_class_name("PZuss")
        # scroll down list follower list
        #print(f"{line} Scroll Buttom  Done!!! {line}")
        links = scroll_box.find_elements_by_tag_name('a')
        sleep(2)
        names = [name.text for name in links if name.text != '']
        #print(f"{line} follower list done!!! {line}")
        # hit close button
        #notworking
        #self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
        #print(f"{line} close Follower  Done!!! {line}")
        #converting = self.converting(names)
        #print(f"{line} convert list to string  Done!!! {line}")
        #print(converting)
        return names

    def quiting(self):
        #print(f"{line} END script BYE!! {line}")
        self.browser.close()

    def getName(self):
        #following = self.following_user()
        #converting = self.converting(following)
        #print(f"{line} Following Name!!{line}")
        #print(converting)
        followers = self.follower_user()
        converting = self.converting(followers)
        print(f"{line} Followers Name!!{line}")
        print(converting)
        #self.textfile(following, 'following')
        self.textfile(followers, 'followers')


        # will see following with follower
        #not_following_back= [user for user in following if user not in followers]
        #print(not_following_back)
    def textfile(self, nameList, type):
        with open('list.txt', 'a') as f:
            #line
            f.write(f"{line} {type} {line} \n")
            for i in nameList:
                f.write(i + '\n')



user_id=input('Enter Your Username:')
password=getpass('Enter Password:')
mybot=InstaBot(user_id, password)
mybot.getName()
mybot.quiting()
