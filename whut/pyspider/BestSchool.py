#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


"""
爬取最好大学网 输出排名前二十的大学
"""


def get_url_resource(url):
    """
    爬取HTML文档返回
    :param url: 资源地址
    :return: HTML
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('捕获异常。')
        return ''


def extract_html_info(html, mylist):
    """
    提取HTML文档中需要的信息，存储到list中
    :param html: HTML文档
    :param mylist: list
    :return: list
    """
    soup = BeautifulSoup(html, 'html.parser')
    info_list = soup.find_all(name='table')
    print(info_list)


def print_info_list(mylist, num=20):
    """
    打印
    :param mylist:
    :return:
    """
    pass


def main():
    mylist = []
    url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = get_url_resource(url)
    extract_html_info(html, mylist)
    print_info_list(mylist)


main()