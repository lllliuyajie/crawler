# coding=utf-8
import multiprocessing as mp
from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin
import time
import re


base_url = 'https://morvanzhou.github.io/'

if base_url !=  'https://morvanzhou.github.io/':
    restricted_crawl = True
else:
    restricted_crawl = False


def crawler(url):
    html = urlopen(url).read().decode('utf-8')
    return html


def prase(html):
    soup = BeautifulSoup(html,features='lxml')
    url = soup.find_all('a', {'href':re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()     # scrip（）移除首尾指定字符
    page_url = set([urljoin(base_url, urls['href']) for urls in url ])  # 去重
    urls = soup.find('meta', {'property': "og:url"})['content']
    return title, page_url, urls


if __name__ == '__main__':
    unseen = set([base_url])   # 未爬过的网页
    seen = set()      # 已经爬过的网页
    count = 0
    t1 = time.time()
    while len(unseen) != 0:
        print(restricted_crawl)
        if restricted_crawl and len(seen) > 20:
            break
        print('爬虫开始\n')
        htmls = [crawler(url) for url in unseen]

        print('解析页面开始\n')
        result = [prase(html) for html in htmls]

        seen.update(unseen)
        unseen.clear()

        for title, page_url, urls in result:
            print(count, title, urls)
            count += 1
            unseen = (page_url - seen)
            print(unseen)
    time2 = time.time()
    print('总的使用时间 %s' % str(time2 - t1))





