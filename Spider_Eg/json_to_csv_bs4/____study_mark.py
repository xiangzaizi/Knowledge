1. json转csv文件
2. 多线程
3. 下一页翻页
4. json load  dumps

5.将字符串拆分数组(split):
var aList = sStr.split();---什么都不传入,默认当成数组中的一个元素. ['12345']
var aList = sStr.split('');---传入空字符串会把每个元素拆分成一个元素. ['1', '2', '3', '4','5']
var aList = sStr.split('-');传入其他字符,字符串中有就会以该字符拆分，没有就会把默认当成数组中的一个元素.

6. 腾讯bs4数据测试
from bs4 import BeautifulSoup
from lxml import etree
import requests

html = requests.get("https://hr.tencent.com/position.php?&start=0", headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}).content

html_obj = etree.HTML(html)
html_obj.xpath("//tr[@class='odd'] | //tr[@class='even']")


soup = BeautifulSoup(html, "lxml")
len(soup.find_all("tr", {"class" : ["even", "odd"]}))
len(soup.find_all(attrs =  {"class" : ["even", "odd"]}))
len(soup.find_all(class_ = ["even", "odd"]))
len(soup.select(".even, .odd"))
len(soup.select("[class='even'], [class='odd']"))

%hist -f xpath_bs4.py  # 保存测试文件
		