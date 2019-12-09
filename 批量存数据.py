# #!/usr/bin/python
# #-*-coding:utf8-*-
# from pymysql import *
# conn=connect(host='117.78.7.54',username='root',password='123456',port=3306,database='student')
# youBiao=conn.cusor()
# ############################################编号#姓名#年龄#性别#系
# youBiao.execute('insert into Student values("{}","{}","{}","{}","{}");')
# conn.commit()
# conn.close()
from wxpy import *
from threading import Timer
import requests
# def get_content():
#     url='http://open.iciba.com/dsapi/'
#     r=request.get(url)
#     print(r)
#     content_e = r.json()['content']
#     content_c = r.json()['note']
#     return content_e,content_c
bot=Bot(cache_path=True)
def send_chat():
    try:
        # content_e,content_c = get_content()
        # print(content_e)
        # 此处填写微信名称
        dear_friend = bot.friends().search(u'燕眸子')[0]
        # 发送的消息
        dear_friend.send('你好')
        # dear_friend.send(centent_c)
        t = Timer(86400, send_chat)
        t.start()
    except Exception as e:
        print('send fail')
if __name__ == '__main__':
    send_chat()