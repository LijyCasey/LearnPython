import requests
import re


URL="http://www.heibanke.com/lesson/crawler_ex02/"
LOGIN_URL="http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/"
se=requests.Session()
res=se.get(LOGIN_URL)
csrf1=res.cookies['csrftoken']
print(res.text)
logindata={'username':'casey','password':'123456'}
logindata['csrfmiddlewaretoken']=csrf1
print(logindata)
response=se.post(LOGIN_URL,logindata)
response=response.content.decode('utf-8')
i=0
while(i<=30):
# for num in range(1,31):
    se.get(URL)
    param={'username':'casey'}
    param['password']=i
    param['csrfmiddlewaretoken']=se.cookies['csrftoken']
    result=se.post(URL,param)
    tmp=re.findall('密码错误',result.content.decode('utf-8'))
    if not tmp:
        print('success: %s'%(i))
        print(result.content.decode('utf-8'))
        break
    i+=1
