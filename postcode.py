# -*- coding: utf-8 -*-

from selenium import webdriver
from lxml import etree
import csv
import pymysql
dir = r'E:\python\csv\posts.csv'
csvFile =open(dir,'w+',newline='')
writer = csv.writer(csvFile)
writer.writerow(['area','post'])

url = 'http://tools.2345.com/yb.htm'
driver = webdriver.Chrome()
driver.get(url)
html = etree.HTML(driver.page_source)

areas_1_xpath = "//tr[2]/td[@class='nobr']//text()" 
posts_1_xpath ="//tr[2]/td[3]"
areas1 = html.xpath(areas_1_xpath)
posts1 = html.xpath(posts_1_xpath)
for area1,post1 in zip(areas1,posts1):
   writer.writerow([area1,post1.text])
# csvFile.close()
for page in range(1,21):
   areas_2_xpath = "//tr[@class='topbr'][{i}]/td[@class='nobr']//text()".format(i=page)
   posts_2_xpath ="//tr[@class='topbr'][{i}]/td[3] ".format(i=page)
  
   areas2 = html.xpath(areas_2_xpath)
   posts2 = html.xpath(posts_2_xpath)
   for area2,post2 in zip(areas2,posts2):
      
      writer.writerow([area2,post2.text])

csvFile.close()