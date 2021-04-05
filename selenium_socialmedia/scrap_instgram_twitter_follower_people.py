'''
Check twitter or IG\s follower and following without login
reference: https://www.youtube.com/watch?v=pPBUWJfquzs
https://github.com/bjcarlson42/youtube/tree/master/2020/5-2020/Python%20Tutorial%20Web%20Scraping%20With%20Selenium%20and%20BeautifulSoup%20%7C%20Python%20One%20Day%20Builds%20-%20Project%201

'''
from bs4 import BeautifulSoup
from selenium import webdriver
import time 
def get_twitter_stats():
    twitter_url = "https://twitter.com/jacklee26"
    driver = webdriver.Chrome('D:\\chromedriver.exe')
    driver.get(twitter_url)
    time.sleep(5)
    content = driver.page_source.encode("utf-8").strip()
    twitter_soup = BeautifulSoup(content, "lxml")
    stats = twitter_soup.findAll("span", class_="css-901oao css-16my406 r-18jsvk2 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0")
    '''
    for stat in stats:
        #strip to remvoe white space
        print(stat.text.strip())
    '''

    following = stats[0].text.strip()
    followers = stats[1].text.strip()
    print("Twitter Stats: {} followers and {} following".format(followers, following))
    

def get_instagram_stats():
    instagram_url = "https://www.instagram.com/chenchihlee/"
    driver = webdriver.Chrome('D:\\chromedriver.exe')
    driver.get(instagram_url)
    time.sleep(5)
    content = driver.page_source.encode("utf-8").strip()
    instagram_soup = BeautifulSoup(content, "lxml")
    stats = instagram_soup.findAll("span")
    posts = stats[1].text.strip()
    followers = stats[2].text.strip()
    following = stats[3].text.strip()
    print(
        "Instagram Stats: {} posts, {} followers, and {} following".format(
            posts, followers, following
        )
    ) 
    
#get_twitter_stats()
get_instagram_stats()