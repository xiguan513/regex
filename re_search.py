#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
search函数试图从整个字符串搜索第一次出现匹配的情况
如果匹配成功，返回一个对象;
如果匹配失败，返回None
"""

"""
输出<a href="http://blog.csdn.net/watsy">watsy's blog</a> 中watsy's blog
"""

from bs4 import BeautifulSoup
import re


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<a href="http://blog.csdn.net/watsy">watsy's blog</a>
"""

soup=BeautifulSoup(html,"html.parser")
#print soup.prettify()
# print soup.title
# print soup.body
#print soup.find_all("a")


def blog_name():
    for i in soup.find_all("a"):
        i=str(i)
        m=re.compile(r'<a.*class=.*')
        if m.search(i) is None:
            m1=re.search(r'.*">(.*)</a>.*',i,re.S)
            return m1.group(1)

print blog_name()

print "=================================="

text = "JGood is a handsome boy, he is cool, clever, and so on..."
m1 = re.search(r'handsome\s', text)
if m1:
    print m1.group()
else:
    print "Not search"

bt1 = ' bat bet bit'

print "=================================="

m1 = re.search('bat', bt1)
if m1 is not None:
    print(m1.group())
else:
    print('m1 not found')