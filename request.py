# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
dir =r'E:\python\csv\test.csv'
csvFile = open(dir,'w+',newline='')
writer = csv.writer(csvFile,delimiter=' ')
writer.writerow(['link'])
pages = set()
lists = []
for temp in range(2,3):
    temp2 = '/'+str(temp)+'.html'
    lists.append(temp2)
    lists.insert(0,'/')
for i in lists:
    url= 'http://www.b2bname.com/product/gangtie/qiye{page}'.format(page=i)
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
  
    links = bs.find_all('a',href=re.compile('^(http://u).*(b2bname\.com/)$'))
    for link in links:
        if link.attrs['href'] not in pages:
            pages.add(link.attrs['href'])
for page in pages:
    writer.writerow(page)
