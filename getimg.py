#encoding=utf-8;
import requests
from bs4 import BeautifulSoup
import urllib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://movie.douban.com/top250'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
res = requests.get(url,headers = header)
soup = BeautifulSoup(res.text, 'html.parser')
imgArr = soup.find_all('img')
for item in imgArr:
    img_src = item.get('src')
    file_name = item.get('alt')
    resImg = requests.get(img_src)
    # 本地保存图片
    urllib.request.urlretrieve(img_src,'/Applications/XAMPP/xamppfiles/htdocs/Python/img/'+file_name+'.jpg')

    
