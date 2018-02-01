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
    tr_tag = soup.tr
    th_list = []
    for tag in tr_tag.children:
        if tag.string != '\n':
            th_list.append(tag.string)
        if len(th_list) == 4:
            break
    mylist.append(th_list)  # 排名的title
    tr_list = soup.tbody.find_all('tr')  # 抓取tbody下所有的tr
    for tr in tr_list:
        data_list = []
        for td in tr.children:  # 遍历tr的子节点，取出前四个值
            if td.string != '\n':
                data_list.append(td.string)
            if len(data_list) == 4:
                mylist.append(data_list)
                break


def print_info_list(mylist, num=30):
    """
    打印爬取信息
    :param mylist: 存储排名信息
    :param num: 打印数量
    :return: None
    """
    template = '{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}'
    print(template.format(mylist[0][0], mylist[0][1], mylist[0][2], mylist[0][3], chr(12288)))
    for i in range(num):
        print(template.format(mylist[i+1][0], mylist[i+1][1], mylist[i+1][2], mylist[i+1][3], chr(12288)))


def main():
    mylist = []
    url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = get_url_resource(url)
    extract_html_info(html, mylist)
    print_info_list(mylist)


main()