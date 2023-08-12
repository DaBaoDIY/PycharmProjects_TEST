# -*- codeing = utf-8 -*-
# @Time : 2022/3/7 8:32
# @Author : XYBDIY
# File : testBS4.py
# @software : PyCharm

"""
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4中：

- Tag
- NavigableString
- BeautifulSoup
- Comment

"""

# 1.Tag  标签以及内容，拿到它所找到的第一个内容
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# file.close()

# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))

# print(bs.title.string)
# print(type(bs.title.string))

# 2.NavigableString  标签里的内容(字符串)

# print(bs.a.attrs)

# bs = BeautifulSoup(html, "html.parser")

# 3.BeautifulSoup   表示整个文档
# print(type(bs))
# print(bs)

# 4.Comment 是一个特殊的NavigableString，输出内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))

#++++++++++++++++++++++++++++++++++++++++++++++++

#文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])

#文档的搜索
#(1)find_all()
#字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list)

import re
# 正则表达式搜索：使用search（）方法来匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)


#方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)

# print(t_list)

# for item in t_list:
#     print(item)


#2. kwargs      参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(href="http://tieba.baidu.com")
# t_list = bs.find_all(class_=True)

# for item in t_list:
#     print(item)

#3.text参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# for item in t_list:
#     print(item)

# t_list = bs.find_all(text = re.compile("\d"))   #应用正则表达式来查找包含特斯那个文本的内容（标签里的字符串）


#4.limit参数

# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)

#css选择器
#通过标签来查找
# t_list = bs.select('title')
#通过类名来查找
# t_list = bs.select('.mnav')
#通过id来查找
# t_list = bs.select('#u1')
#通过属性来查找
# t_list = bs.select("a[class='bri']")
#通过子标签查找
# t_list = bs.select("head > title")

t_list = bs.select(".mnav~ .bri")
print(t_list[0].get_text())

# for item in t_list:
#     print(item)











