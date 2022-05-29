# Download images from a website
## Description: 
- 1. go to url
> url = 'https://www.nthu.edu.tw/'
- 2. parse url wen 
r = requests.get(url=url, headers=headers)
print(r)
soup = BeautifulSoup(r.text, 'html.parser')
- 3. find image contain `img` and `png` using `for loop`
> for img in soup.findAll('img'):
> for img in soup.findAll('png'):

### Framework: 
- BeautifulSoup
> import requests
> from bs4 import BeautifulSoup

### Reference
- [Refer related youtube tutorial](https://www.youtube.com/watch?v=yX30pRkEyV4&t=817s)

