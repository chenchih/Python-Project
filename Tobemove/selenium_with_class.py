from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class test():
    def __init__(self):
        self.browser=webdriver.Chrome('D:\\chromedriver.exe')
        self.browser.maximize_window()
        self.browser.get('https://www.google.com')
        element= self.browser.find_element_by_class_name('gLFyf.gsfi')
        element.send_keys('test')            
        element.submit() 
        sleep(10)

def main():
    mytest=test()
if __name__ == '__main__':
    main()

 
