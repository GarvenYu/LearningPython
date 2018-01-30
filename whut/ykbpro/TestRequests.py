#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import ssl


def get_pic(url):

    """
    爬取豆瓣网的一张电影剧照
    :param url: 资源地址
    :return: None
    """

    file_name = url.split('/')[-1]
    root_path = 'G:\\pycharm_examples\\pic\\'
    file_path = root_path + file_name
    if not os.path.exists(root_path):
        os.mkdir(root_path)
    if not os.path.exists(file_path):
         try:
            header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
                      'Referer': url,
                      'Host': 'img3.doubanio.com'
                      }
            r = requests.get(url, headers=header)
            print(r.request.headers)
            r.raise_for_status()
            r.encoding = 'UTF-8'
            with open(file_path, 'wb') as f:
                f.write(r.content)
         except:
             print('捕获异常')
    else:
        print('文件已存在')


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    get_pic('https://img3.doubanio.com/view/photo/raw/public/p2508926095.jpg')