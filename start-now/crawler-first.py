# coding=utf-8
'''from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode("utf-8")
soup = BeautifulSoup(html, features='lxml')

all_href = soup.find_all("a")
all_href = [l['href']for l in all_href]

print(all_href)'''

'''from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen('https://morvanzhou.github.io/static/scraping/list.html').read().decode('utf-8')
# print(html)
soup = BeautifulSoup(html, features='lxml')

month = soup.find_all('li', {'class': 'month'})
for i in month:
    print(i.get_text())
jan = soup.find_all('ul', {'class': 'jan'})
for i in jan:
    print(i.get_text())'''
'''from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = 'https://baike.baidu.com'
history = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(5):
    url = base_url + history[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    print(soup.find('h1').get_text(), '  ulr: '+(base_url+history[-1]))

    sub_url = soup.find_all('a', {'target': "_blank", "href": re.compile("/item/(%.{2})+$")})
    print(sub_url)

    if len(sub_url) != 0:
        # print(random.sample(sub_url, 1)) # 一个<a href ="", target = "" > 算是一个长度 加入列表中也算一个长度 取出列表中的第0个位置的href的值
    # [<a href="/item/%E8%B6%85%E6%96%87%E6%9C%AC" target="_blank">超文本</a>]
        history.append(random.sample(sub_url, 1)[0]["href"])
    else:
        history.pop()'''   # 爬百度百科

'''param = {"wd": "莫烦Python"}
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
webbrowser.open(r.url)'''


'''data = {'firstname': "莫烦", "lastname": "周"}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=data)
print(r.text)
webbrowser.open(r.url)
r = requests.get('http://pythonscraping.com/files/processing.php', cookies = r.cookies)
print(r.text)
webbrowser.open(r.url)'''
# 每次传递cookies麻烦，所以使用session会话
'''session = requests.session()
poyload = {'firstname': "莫烦", "lastname": "周"}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=poyload)
print(r.cookies.get_dict())

r = session.get('http://pythonscraping.com/pages/cookies/welcome.php')'''
import requests
from bs4 import BeautifulSoup

URL = 'http://www.nationalgeographic.com.cn/animals/'

html = requests.get('http://www.nationalgeographic.com.cn/animals/').text
soup = BeautifulSoup(html, features="lxml")
img_list = soup.find_all('ul', {"class": "img_list"})
# print(img_list) 如果选取的标签ul 属于父标签，接着会返回次标签和字标签

for img_url in img_list:
    imgs = img_url.find_all("img")
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream = True)
        img_name =url.split('/')[-1]
        with open("E:\L python\img\%s" % img_name, 'wb') as  file:
            for chunk in r.iter_content(chunk_size=128):
                file.write(chunk)






