#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
爬取淘宝网宝贝输出价格和名称
"""
import re
import requests


def get_url_resource(url):
    """
    爬取淘宝网HTML网页,返回文本。
    :param url:资源链接
    :return:文本
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text
    except:
        print('发生异常。')
        return ''


def parse_html_text(text, infolist):
    re_title = re.compile(r'\"title\":\".*?\"')
    re_price = re.compile(r'\"price\":\"\d{3,5}\"')
    titlelist = re_title.findall(text)
    pricelist = re_price.findall(text)


def main():
    mylist = []
    url = 'https://s.taobao.com/search?q=手机'
    text = get_url_resource(url)
    parse_html_text(text, mylist)


main()