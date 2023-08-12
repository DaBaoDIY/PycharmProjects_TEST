# -*- codeing = utf-8 -*-
# @Time : 2022/3/6 23:38
# @Author : XYBDIY
# File : testUrllib.py
# @software : PyCharm

import urllib.request
#获取一个get请求
# response =  urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码


#获得一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response =  urllib.request.urlopen("http://www.baidu.com",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except Exception as e:
#     print("time out!")

# 返回状态码
# response =  urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# print(response.getheader("Server"))

#模拟浏览器访问，进行伪装
# url = "http://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30"
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding='utf-8')
# #封装成一个对象
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

#模拟浏览器访问豆瓣网
url = "https://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))