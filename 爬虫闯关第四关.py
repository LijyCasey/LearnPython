#coding=utf-8
'''
使用多线程
'''
import requests
import threading
import re
import queue

data={'username':'casey','password':'123456'}
url='http://www.heibanke.com/lesson/crawler_ex03/'
login_url='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
passwd_url='http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page=%s'

session=requests.Session()
r1=session.get(login_url)
# print(r1.text.encode('utf-8'))
csrftoken=r1.cookies['csrftoken']
# print(csrftoken)
# print(r1.cookies.items())
data['csrfmiddlewaretoken']=csrftoken
response=session.post(login_url,data)
csrftoken=response.cookies['csrftoken']
#
data2={'username':'casey','csrfmiddlewaretoken':csrftoken}
# print(passwd_url% "1")
# url2=passwd_url% "1"
# r2=session.get(url2,cookies=response.cookies)
# print(r2.text)
def getpasswd(page):
    tmp_url=(passwd_url %(page))
    print(tmp_url)
    r2=session.get(tmp_url,cookies=response.cookies)
    pos_re=re.compile(r'<td data-toggle="tooltip" data-placement="left" title="password_pos">(\d+)</td>')
    val_re=re.compile(r'<td data-toggle="tooltip" data-placement="left" title="password_val">(\d+)</td>')
    pos=pos_re.findall(r2.text)
    val=val_re.findall(r2.text)
    for i in range(len(pos)):
        dict[int(pos[i])]=val[i]
        # q.put('ok')
        print(len(dict))
dict={}
getpasswd(1)
print(dict.items())
print(sorted(dict))
# q=queue.Queue()
# python可以先使用一个变量之后再声明？
# 还真可以
# for i in range(1,3):
#     q.put('ok')

# while len(dict)!=100:
#     for page in range(1,14):
#         if q.get():
#             t=threading.Thread(target=getpasswd,args=(page,))
#             t.start()
#         if len(dict)==100:
#             break
# passwd=''
# ks=sorted(dict)
#
#
# for k in ks:
#     print(k,dict[k])
#     passwd=passwd+dict[k]
# print(passwd)
# data2['password']=passwd
# r5=session.post(url,data=data2)
# print(r5.text)
