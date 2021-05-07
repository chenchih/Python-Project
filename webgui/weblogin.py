import time
from selenium import webdriver
try:
    # Chrome with https
    Path_ = 'D:\\test\\selenium\\chromedriver.exe'
    
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument('start-maximized')
    driver = webdriver.Chrome(Path_, chrome_options=options)   
    driver.get("http://google.com/")
except:
    print ("Select browser fail")
    driver.quit()
    sys.exit(1)
