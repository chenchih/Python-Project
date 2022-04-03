# get follower and following list

### Description

This is a automation to your account, and get your follower and following list. 

### Note:

- If not working, maybe Instagram had changed their structure. 

- Most of the time not working should be the scrolling follower or following, please check on it:

```
#following
scroll_box = self.browser.find_element_by_xpath("//div[@class='isgrP']")
#follower
scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
```

### Step

1. execute the script
2. (user enter)enter your username, and password(password will be hidden)
3. open instagram url
3. login your account
4. go to your profile page
5. click on following
6. scroll down to the end
8. start to capture user list
9.  convert list to string
10.  click on follower
11. scroll down to the end
12. start to capture user list
13.  convert list to string

### Update

- inital release 

- not working 

  ```
  #following 
  scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
  .....
  self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
  
  #follower
  self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
  ```

- 202204: update follower and following scroll and close button 

  ```
  #following
  scroll_box = self.browser.find_element_by_xpath("//div[@class='isgrP']")
  #follower
  scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
  ```

  

### manual test 

```
from selenium import webdriver
from time import sleep
from getpass import getpass
from datetime import datetime
option = webdriver.ChromeOptions()
option.add_argument('--lang=en-US')
driverPath = 'C:\\webdriver\\chromedriver.exe'
browser=webdriver.Chrome(driverPath,chrome_options=option)
browser.get("http://instagram.com")
```

