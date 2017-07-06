import urllib.request
import re

url="http://www.heibanke.com/lesson/crawler_ex00/"
data=urllib.request.urlopen(url).read()
data = data.decode('utf-8')
# print(data)
ruler=re.compile(r'数字[^\d]*(\d+)')
number=ruler.findall(data)
index=1
# print(number[0])
while(number):
    url2=url+number[0]
    print(url2)
    data=urllib.request.urlopen(url2).read()
    data=data.decode('utf-8')
    number=ruler.findall(data)
    print("web: %s" %(url2))
else:
    print ("next: %s" %(url2))
