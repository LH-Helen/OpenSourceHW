# OpenSourceHW

This is a homework for the Open Source Software Foundation course.

## 框架
python-3.7

BeautifulSoup

flask-2.0.2

pymysql-1.0.2

## 目录结构
Beike_data：贝壳网数据爬取以及存储
- Beike.ipynb：贝壳网数据爬取
- BeikeMysql.ipynb：数据库存储
- beijing_loupan_data：北京楼盘数据
  - beijing_loupan_data_middle：处理数据格式
  - beijing_loupan_data_orginal：初始爬取数据
  - beijing_loupan_final.csv：数据整合
- beike_loupan.sql：北京楼盘数据库


Beike_flask：flask web
- static：echart.min.js(暂时没用到)
- templates：html文件夹
- mysql.py: 连接数据库以及数据库操作
- test.py：后端连接


venv：虚拟环境创建

## 创建虚拟环境

## 爬取数据
利用BeautifulSoup工具对北京楼盘 'https://bj.fang.ke.com/loupan/' 的各个地区进行爬取，分别将数据存储到文件中。

整合数据，并存入数据库beike_loupan，表名为beijing_loupan。数据包括名字、地区、价格、最低总价、最高总价、是否VR看房。

## flask+echart+mysql实现数据可视化
利用flask框架搭建Web程序应用。并连接mysql数据库获取数据。

利用echart，将数据以图表形式可视化。

## 人员
BY Liu He

BY Yang Xiaohan

BY WYB TWINKLE

BY Wu Anqi

BY Ma Yan
