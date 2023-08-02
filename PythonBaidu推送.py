import requests
from bs4 import BeautifulSoup

import os
import json
import time

web_head = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36 Edg/81.0.416.34',
    'Content-Type': 'text/plain'
}
params = {
    'site': 'wangyuzhen666.github.io',
    'token': 'FbTpyDkXWgtBj02l'
}


url = 'http://' + params['site']


def urls_file(urls):
    if not os.path.isfile("./sitemaps.txt"):
        file = open("./sitemaps.txt", 'w')
        for i in range(len(urls)):
            file.write(urls[i] + '\n')
        data = file.read()
        file.close()
        return data
    else:
        temp = []
        file = open("./sitemaps.txt", 'r+')
        data = file.readlines()

        for i in range(len(urls)):
            if urls[i] + '\n' not in data:
                temp.append(urls[i] + '\n')
        data = temp
        file.close()
        file = open("./sitemaps.txt", 'a')
        for i in range(len(data)):
            file.write(data[i])
        file.close()
        return data


def get_urls():
    try:
        data = requests.get(url)
        urls = []

        if data.status_code == 200:
            soup = BeautifulSoup(data.text, 'html.parser')
            link = soup.find_all('a')

            for a in link:
                hreflink = a.get('href')
                if hreflink and url in hreflink and '#' not in hreflink:
                    urls.append(hreflink)
            return list(set(urls))
        else:
            raise Exception(
                "Bad status:Please check whether the website can be accessed normally"
            )
    except Exception as result:
        print(result)


def post_urls(data):
    strs = ''
    for i in range(len(data)):
        strs += data[i]
    print(strs)
    info = requests.post('http://data.zz.baidu.com/urls',
                         data=strs,
                         params=params,
                         headers=web_head)
    if int(info.text[9:12]) == 400:
        return "No submissions need to be updated or site error or over quota"
    if int(info.text[9:12]) == 401:
        return "Token is not valid"
    if int(info.text[9:12]) == 404:
        return "Api is not found"
    if int(info.text[9:12]) == 500:
        return "Internet error"
    else:
        return info.text


def main():
    while True:
        file = open("./post.data", 'a')
        post_data = post_urls(urls_file(get_urls()))
        #print(post_data)
        file.write(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':' +
            post_data + '\n')
        file.close()
        time.sleep(3600)


main()

