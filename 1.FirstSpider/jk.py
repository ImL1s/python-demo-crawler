#-*_coding:utf8-*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'開始爬取內容...'.encode('utf-8')

    def getsource(self,url):
        html = requests.get(url)
        return html.text

    def changepage(self,url,totoal_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,totoal_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group

    def geteveryclass(self,source):
        everyclass = re.findall('(<li id="\d*" .*?</li>)',source,re.S)
        return everyclass

    def getinfo(self,eachclass):
        info = {}
        info['title'] = re.search('target="_blank" jktag=".*?">[^ \n<](.*?)</a>',eachclass[0],re.S).group(1)
        
        return info;
    


if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jkspider = spider()
    all_links = jkspider.changepage(url,10)
    
    html = jkspider.getsource(all_links[0])
    aclass = jkspider.geteveryclass(html)
    info = jkspider.getinfo(aclass)
    
    # print all_links
    # print(all_links[0])
    # print html.encode('utf-8')
    # print aclass[0].encode('utf8')
    print info['title'].encode('utf8')

