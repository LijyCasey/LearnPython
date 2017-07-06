import itchat
from itchat.content import TEXT

@itchat.msg_register(itchat.content.TEXT)
def simple_reply(msg):
    return msg['Text']

itchat.auto_login(hotReload=True)
#itchat.search_friends()
itchat.run()
