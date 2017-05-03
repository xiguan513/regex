#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
腾讯电影抓取前几页电影显示连接以及评分

"""


from bs4 import BeautifulSoup

import urllib2
import urllib
import re
import time

url=''

class pachong(object):

    def __init__(self):

        self.url='http://v.qq.com/x/list/movie'
        self.user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers={'User-Agent': self.user_agent}

    def getPage(self):
        request = urllib2.Request(self.url, headers=self.headers)
        response = urllib2.urlopen(request)
        connect = response.read().decode('utf-8')
        page = BeautifulSoup(connect, "html.parser")

        for p in page.find_all("a"):
            p = str(p)
            p1 = re.compile(r'<a.*paging_page_\d.*href=.*\;(?P<page_url>.*)">(?P<page_num>\d+).*')
            if p1.search(p) is not None:
                yield (p1.search(p).group('page_url'),p1.search(p).group('page_num'))


    def movie_name(self):
        for i in self.getPage():
            url="http://v.qq.com/x/list/movie?&%s" % (i[0])

            try:
                request = urllib2.Request(self.url, headers=self.headers)
                response = urllib2.urlopen(request)
                connect = response.read().decode('utf-8')
                # print content
                pattern = re.compile('class="figure_title">(.*?)target=".*?title">(.*?)</.*?score_l">(.*?)</div', re.S)
                items = re.findall(pattern, connect)
                for movie in items:
                    score = movie[2].encode("utf-8").strip("\n")
                    pattern1 = re.compile('(.*?)</em>.*?score_s">(.*?)</em>', re.S)
                    items1 = re.findall(pattern1, score)
                    print "电影连接： %s  电影名称： %s  " % (
                        movie[0].encode('utf-8').strip("\n"), movie[1].encode('utf-8').strip("\n"))
                    for num in items1:
                        num = num[0] + num[1]
                        print "评分： %s" % num
                print "=================第%s页所有电影====================" % i[1]
            except urllib2.URLError, e:
                if hasattr(e, "code"):
                    print e.code
                if hasattr(e, "reason"):
                    print e.reason

    def start(self):
        self.movie_name()


if __name__=="__main__":
    a=pachong()
    a.start()