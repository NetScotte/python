import requests
import json


# 利用requests针对示例网站的评论进行查看，提交，修改，删除等操作


# 查看评论
r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
c = json.loads(r.text)
print(c['title'])
print(c['comments'])
# 上下部分实现的功能一致，使用下面的更简洁
# try:
#     comments = r.json()
#     print(comments[u'title'])
#     print(comments[u'comments'])
# except:
#     pass

# 以上代码知道了title和该title下的commnets数量，commnets在其他网站.获取最后一条评论
# r = requests.get(r.url+u'/comments')
# print(r.status_code)
# comments = r.json()
# print(comments[0].keys())
# print(comments[9][u'body'])
# print(comments[9][u'user'][u'login'])

# 针对该comments发表评论，由于身份错误，以下行为均只能再使用真实身份后进行
# body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
# print(body)
# url = u"https://api.github.com/repos/kennethreitz/requests/issues/482/comments"
# 
# auth = requests.auth.HTTPBasicAuth('','not_a_real_password')
# r = requests.post(url=url,data=body,auth=auth)
# print(r.status_code)
# comments = r.json()
# print(comments)

# 修改评论
# print(comments[u"id"])
# 5804413
#
# body = json.dumps({u"body": u"Sounds great! I'll get right on it once I feed my cat."})
# url = u"https://api.github.com/repos/kennethreitz/requests/issues/comments/5804413"
#
# r = requests.patch(url=url, data=body, auth=auth)
# r.status_code
# 200

# 删除评论
# r = requests.delete(url=url, auth=auth)


