# -*- codeing = utf-8 -*-
# @Time : 2022/3/7 23:49
# @Author : XYBDIY
# File : testRe.py
# @software : PyCharm


#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
#创建模式对象
pat = re.compile("AA")  #此处的AA，是正则表达式，用来去验证其他的字符串
# m = pat.search("CBA")          #search字符串被校验的内容

# m = pat.search("ABCAA")

# 没有模式对象
# m = re.search("asd","Aasd")   #前面的字符串是规则（模板），后面的字符串是被校验的的对象
# print(m)

#print(re.findall("a","ASDaDFGAa"))  #前面的字符串是规则（正则表达式），后面的字符串是被校验的的字符串

# print(re.findall("[A-Z]","ASDaDFGAa"))   #找到后面字符串中大写的字母

# print(re.findall("[A-Z]+","ASDaDFGAa"))    #['ASD', 'DFGA']


#sub
# print(re.sub("a","A","abcdaag"))     #小a用大A替换，在第三个字符串中查找

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r"\aadb-\'"
print(a)
