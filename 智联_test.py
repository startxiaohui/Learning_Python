import requests
import json
import random
from lxml import etree
url = 'https://sou.zhaopin.com/?jl=530&kw=python&kt=3'
useragent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko']

res = requests.request('get', url, headers={'User-agent':random.choice(useragent_list)})

with res:
    txt = res.text
    xml_test = etree.HTML(txt)
    title = xml_test.xpath("//script[2]")
    for t in title:
        txt = t.xpath('.//text()')
        if len(txt) == 0:continue
        #获取网页上的随机字符串
        randow_str = ''.join(map(lambda x:x.strip(),txt)).split('"')[1].split('-')[0]
