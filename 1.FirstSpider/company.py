#-*-coding:utf8-*-
import requests
import re


for index in range(4)
    

url1 = 'https://www.crowdfunder.com/?q=filter&page=1'
url2 = 'https://www.crowdfunder.com/?q=filter&page=2';

html = requests.get(url1).text
html += requests.get(url2).text
# print html.encode('utf8')

title = re.findall('<div class="card-title">(.*?)</div>',html,re.S)

for each in title:
    print each.encode('utf8')




