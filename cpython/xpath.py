import requests
from lxml import etree
from selenium import webdriver

query = '刘嘉玲'
'''下载全部图片'''
def download(src,id):
    dir = 'E:\\python\\liujialing\\'+ str(id) +'.jpg'
    try:
        pic = requests.get(src,timeout = 10)
        fp = open(dir,'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')
src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
start = 0
end = 15
limit = 15
for i in range(start,end,limit):
    url = 'https://search.douban.com/movie/subject_search?search_text='+query+'&cat=1002&start='+str(i)
    driver = webdriver.Chrome()
    driver.get(url)
    html = etree.HTML(driver.page_source)
    srcs = html.xpath(src_xpath)
    titles = html.xpath(title_xpath)
    for src,title in zip(srcs,titles):
        download(src,title.text)