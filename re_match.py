#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
match函数试图从字符串的起始部分对模式进行匹配
如果匹配成功，返回一个匹配对象；
如果匹配失败，返回None
match参数
第一个参数是正则表达式，这里为"(\w+)\s"，如果匹配成功，则返回一个Match，否则返回一个None；
第二个参数表示要匹配的字符串；
第三个参数是标致位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
"""

import re

#通过正则进行匹配
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s", text)
print 'match'
if m:
    print m.group(0), '\n', m.group(1)
else:
    print "Not match"

print "===================================="
#匹配起始部分
bt = 'bat bet bit'
m = re.match('bat', bt)

if m is not None:
    print(m.group())
else:
    print("Not found bat")


n = re.match('bit', bt)
if n is not None:
    print(n.group())
else:
    print("Not found bit")

print "===================================="
#通过正则扩展方法匹配字符串
text = 'kitty kitty'
w = re.match(r'\b(?P<word>\w+)\b\s+(?P=word)', text)#通过扩展指定需要匹配字符串的别名，可以后续调用

print "字典",w.groupdict()#字典模式输出
print w.group()
print "指定序列号",w.group(1)
print "指定名称",w.group('word')
