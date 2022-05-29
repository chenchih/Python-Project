#https://www.youtube.com/watch?v=yX30pRkEyV4&t=817s
import requests
from bs4 import BeautifulSoup
import os
url = 'https://www.nthu.edu.tw/'
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

r = requests.get(url=url, headers=headers)
print(r)
soup = BeautifulSoup(r.text, 'html.parser')

i = 0

for img in soup.findAll('img'):
    i = i + 1

    image_temp = img.get('src')
    print(image_temp)
    if image_temp[:1] == '/':
        image_path = "https://www.nthu.edu.tw" + image_temp
        
    else:
        #image_path = image_temp
        image_path = "https://www.nthu.edu.tw/public" + image_temp
    #print(image_path)

    file_name_temp = img.get('alt')
    #print(file_name_temp)  

    if len(file_name_temp) == 0:
        file_name = str(i)
    else:
        file_name = file_name_temp
    #print(file_name)

    if '.jpg' in image_path:
        c_wd = os.getcwd()

        try:
            os.makedirs('Images/JPEG')
        except:
            folder_dir = c_wd + '/Images/JPEG'
            name_file = "{}.jpg".format(file_name)

            final_path = os.path.join(folder_dir, name_file)

            with open(final_path , 'wb') as f:
                f.write(requests.get(image_path).content)
    

    if '.png' in image_path:
            c_wd = os.getcwd()
            try:
                os.makedirs('Images/PNG')
            except:
                folder_dir = c_wd + '/Images/PNG'
                name_file = "{}.png".format(file_name)

                final_path = os.path.join(folder_dir, name_file)

                with open(final_path , 'wb') as f:
                    f.write(requests.get(image_path).content)
