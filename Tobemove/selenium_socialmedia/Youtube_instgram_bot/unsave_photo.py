"""
Title:How to unsave all instagram posts | python tutorial
Link: https://www.youtube.com/watch?v=TmLth2SvCs8&t=218s
Youtuber/author: Max Codez
status: TEST PASS 
"""
from selenium import webdriver
from time import sleep
driverPath = 'D:\\test\\chromedriver.exe'
driver = webdriver.Chrome(driverPath)
def Login(user, passw):
    driver.get("https://instagram.com")
    sleep (4)
    driver.find_element_by_name('username').send_keys(user)
    driver.find_element_by_name('password').send_keys(passw)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(4)
    unsave_photo()
def unsave_photo():
    driver.get("https://instagram.com/chenchih.test/saved/all_posts/")
    sleep(5)
    div = driver.find_elements_by_class_name("v1Nh3")
    div[0].find_element_by_tag_name("a").click()
    sleep(3)
    for i in range(2):
        driver.find_element_by_xpath("//span[@class=\"wmtNn\"]").click()
        driver.find_element_by_xpath("//a[@class=\" _65Bje  coreSpriteRightPaginationArrow\"]").click()
        #driver.find_element_by_xpath("//a[@class=' _65Bje  coreSpriteRightPaginationArrow']").click()
        #https://www.instagram.com/p/COXYA-NnXGD/
                                                        
        sleep(2)
    print("end")
    driver.quit()
    

#Login(input("user: "),input("password: ") )
Login ('username', 'password')
sleep(3) 


