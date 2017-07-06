import urllib.request
import re

data={'username':'casey'}
url="http://www.heibanke.com/lesson/crawler_ex01/"
for num in range(1,31):
    data['password']=num
    post_data=urllib.parse.urlencode(data).encode(encoding='utf_8')
    print(post_data)
    response=urllib.request.urlopen(url,post_data)
    html=response.read()
    html=html.decode('utf-8')
    # print(html)
    result=re.findall('密码错误',html)
    if not result:
        print (html +" success")
        break
