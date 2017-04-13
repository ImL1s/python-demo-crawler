#-*-coding:utf8-*-
import requests
import re
import sys
reload(sys)

sys.setdefaultencoding("utf-8")
type = sys.getfilesystemencoding()

# add a header
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

# http://jp.tingroom.com/yuedu/yd300p/
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers = hea)
html.encoding = 'utf-8'

# find japenese content
title = re.findall('color:#666666;">(.*?)</span>',html.text,re.S)

for each in title:
    print each.encode('utf-8')

# find chinese title
chinese = re.findall('style="color: #039;">(.*?)</a>',html.text,re.S)

for each in chinese:
    print each.encode('utf-8')
