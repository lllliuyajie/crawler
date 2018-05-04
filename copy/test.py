from bs4 import  BeautifulSoup
import requests
import os
URL = 'http://www.nationalgeographic.com.cn/animals/'
html = requests.get(URL).text
soup = BeautifulSoup(html, features="lxml")
img_list = soup.find_all("ul", {"class": "img_list"})
for img in img_list:
    imgs = img.find_all("img")
    print(imgs)
    for img_url in imgs:
        img_urls = img_url["src"]
        r = requests.get(img_urls, stream = True)
        img_name = img_urls.split("/")[-1]
        print(img_name)
        with open("../img/image%s " % img_name, 'wb') as file:    # %s% 允许插入    "%s ,%s" %(str, str)
            for chunk in r.iter_content(chunk_size=128):
                file.write(chunk)
            print("Saved%s"%img_name)
