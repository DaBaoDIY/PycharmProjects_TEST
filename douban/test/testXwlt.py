# -*- codeing = utf-8 -*-
# @Time : 2022/3/8 21:36
# @Author : XYBDIY
# File : testXwlt.py
# @software : PyCharm

cm
'''
wookbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
wooksheet = wookbook.add_sheet('sheet')     #创建工作表
wooksheet.write(0,0,'hello')                #写入数据，第一行参数“行”，第二个参数“列”，第三个参数内容
wookbook.save('student.xls')                #保存数据表
'''

wookbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
wooksheet = wookbook.add_sheet('sheet')     #创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        wooksheet.write(i,j,"%d * %d = %d "%(i+1,j+1,(i+1)*(j+1)))
wookbook.save('student.xls')                #保存数据表