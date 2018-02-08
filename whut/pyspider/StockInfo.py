#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
爬取东方财富网和百度股票网，输出每只股票的信息。
"""
import re
import requests
from bs4 import BeautifulSoup
import os


def request_template(url):
    """
    调用requests库通用模板
    :param url: 资源链接
    :return: text
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text
    except:
        print('error')


def get_url_resource(url):
    """
    爬取东方财富网获取股票编号
    :param url:资源地址
    :return:list
    """
    stock_list = []
    regex = re.compile(r'[s][hz]\d{6}')
    html = request_template(url)
    bs = BeautifulSoup(html, 'html.parser')
    for link_a in bs.find_all('a'):
        try:
            stock_num = regex.findall(link_a.attrs['href'])[0]
            stock_list.append(stock_num)
        except:
            continue
    print(stock_list)
    return stock_list


def get_stock_info(stock_list, stock_info_url, file_path):
    """
    根据股票编号获取每只股票的详情
    :param stock_list: 股票编号列表
    :param stock_info_url: 股票详情链接
    :param file_path:本地文件路径
    :return: list
    """
    info_list = []
    try:
        for stock_num in stock_list:
            info_dict = {}
            url = stock_info_url+stock_num+'.html'
            html = request_template(url)
            bs = BeautifulSoup(html, 'html.parser')
            stock_name = bs.find('a', attrs={'class': 'bets-name'}).text.split(' ')[0] ---
            info_title = bs.find_all('dt')
            info_data = bs.find_all('dd')
            for i in range(len(info_title)):
                key = info_title[i].string ---
                value = info_data[i].string
                info_dict[key] = value
            info_dict[stock_num] = stock_name
            info_list.append(info_dict)
        return info_list
    except:
        print('ERROR')


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    file_path = os.path.join(os.path.abspath('.'), 'stock_info.txt')
    stock_list = get_url_resource(stock_list_url)
    info_list = get_stock_info(stock_list, stock_info_url, file_path)
    for i in info_list:
        print(info_list[i]+'\n')


main()
