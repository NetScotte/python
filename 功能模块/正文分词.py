import re
import jieba
import jieba.analyse

s=''
with open('../dataset/data/normal/10') as f:
    blank_pattern= re.compile(r'^$')                        #匹配空行
    tag=0
    content=[]
    for i in f:
        if blank_pattern.match(i) and tag==0:
            tag=1
        if tag==1:
            content.append(i)
    s=''.join(content)   

#tags=jieba.cut(s)
tags=jieba.analyse.extract_tags(s,30,allowPOS=('ns', 'n', 'vn', 'v'))
print('\\'.join(tags))
    
