from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
history = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(10):
    url = base_url+history[-1]
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features="lxml")
    print(i, soup.find("h1").get_text(), "url:"+history[-1])
    print(soup.find('h1'))

    sub_urls = soup.find_all("a", {"target": "_blank", "href":  re.compile("/item/(%.{2})+$")}) #列表中的字典  一个<a ....>是列表，而href和targt是字典的key
    print(sub_urls)
    if len(sub_urls) != 0:
        history.append(random.sample(sub_urls, 1)[0]["href"])
    else:
        history.pop()
   # print(history)
