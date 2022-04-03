'''
https://www.youtube.com/watch?v=d2GBO_QjRlo
update: 2022
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
        sleep(3)
        
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
        self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        #print(f"{line} Login In Success!!! {line}")
        sleep(5)
        self.browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(3)
        self.browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        #print(f"{line} Not Saving Done!!! {line}")
        sleep(3)
        #click on profile page
        self.browser.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
        #print(f"{line} Profile  Done!!! {line}")
        sleep(2)

    def converting (self, nameList):
        IGuserName = "\n".join(nameList)
        return IGuserName

    def following_user(self):
        #click on following button(People you are following; people you like)
        self.browser.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        #print(f"{line} click on following !!! {line}")
        sleep(2)
        # copy the xpath of scrollbar
        #not working
        #scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
        scroll_box = self.browser.find_element_by_xpath("//div[@class='isgrP']")
        sleep(5)
        # height variable
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            # scroll down and retrun the height of scroll
            ht = self.browser.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)
        # list follower name
        sleep(5)
        #print(f"{line} Scroll Buttom  Done!!! {line}")
        links = scroll_box.find_elements_by_tag_name('a')
        sleep(2)
        names = [name.text for name in links if name.text != '']
        # need to filter empty string so we used name.text instead of name
        print(names)
        #print(f"{line} follower list done!!! {line}")
        # hit close button
        #self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
        #print(f"{line} close Follower  Done!!! {line}")

        #convert list to string
        converting = self.converting(names)
        print(f"{line} convert list to string  Done!!! {line}")
        print(converting)
        print(f"{line} Printing name  {line}")
        #self.quiting()


    def follower_user(self):
        #clik on follower (people who follow you)
        self.browser.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
        print(f"{line} Follower  Done!!! {line}")
        sleep(2)
        # copy the xpath of scrollbar
        #scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/ul/div")
        scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")



        # you can also use either one below
        # scroll_box= self.browser.find_element_by_xpath("//div[@class='PZuss']")
        # scroll_box=self.browser.find_element_by_class_name("PZuss")

        # list follower name
        #print(f"{line} Scroll Buttom  Done!!! {line}")
        links = scroll_box.find_elements_by_tag_name('a')
        sleep(2)
        names = [name.text for name in links if name.text != '']
        # need to filter empty string so we used name.text instead of name
        print(names)
        print(f"{line} follower list done!!! {line}")
        # hit close button
        #not working
        #self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()

        print(f"{line} close Follower  Done!!! {line}")

        #current not doing this yet: this item is to check who is not following back
        ############################
        # will see following with follower
        #not_following_back= [user for user in following if user not in followers]
        #print(not_following_back)

        converting = self.converting(names)
        print(f"{line} convert list to string  Done!!! {line}")
        print(converting)
        print(f"{line} Printing name  {line}")
        #self.quiting()

         
    def quiting(self):
        print(f"{line} END script BYE!! {line}")
        self.browser.close()


             

user_id=input('Enter Your Username:')
password=getpass('Enter Password:')
#user_id=""
#password=""
mybot=InstaBot(user_id, password)
#mybot.following_user()
mybot.follower_user()
mybot.quiting()
#mybot.get_unfollower()
#future add unfollowing, unsave, save, get to list, excel
