import requests
import json


# ����requests���ʾ����վ�����۽��в鿴���ύ���޸ģ�ɾ���Ȳ���


# �鿴����
r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
c = json.loads(r.text)
print(c['title'])
print(c['comments'])
# ���²���ʵ�ֵĹ���һ�£�ʹ������ĸ����
# try:
#     comments = r.json()
#     print(comments[u'title'])
#     print(comments[u'comments'])
# except:
#     pass

# ���ϴ���֪����title�͸�title�µ�commnets������commnets��������վ.��ȡ���һ������
# r = requests.get(r.url+u'/comments')
# print(r.status_code)
# comments = r.json()
# print(comments[0].keys())
# print(comments[9][u'body'])
# print(comments[9][u'user'][u'login'])

# ��Ը�comments�������ۣ�������ݴ���������Ϊ��ֻ����ʹ����ʵ��ݺ����
# body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
# print(body)
# url = u"https://api.github.com/repos/kennethreitz/requests/issues/482/comments"
# 
# auth = requests.auth.HTTPBasicAuth('','not_a_real_password')
# r = requests.post(url=url,data=body,auth=auth)
# print(r.status_code)
# comments = r.json()
# print(comments)

# �޸�����
# print(comments[u"id"])
# 5804413
#
# body = json.dumps({u"body": u"Sounds great! I'll get right on it once I feed my cat."})
# url = u"https://api.github.com/repos/kennethreitz/requests/issues/comments/5804413"
#
# r = requests.patch(url=url, data=body, auth=auth)
# r.status_code
# 200

# ɾ������
# r = requests.delete(url=url, auth=auth)


