import re

#提取源ip地址，发送者邮箱地址，以及邮件正文
with open('../dataset/data/normal/10') as f:
    rec_pattern = re.compile(r'Received:')
    fro_pattern = re.compile(r'From:')
    ip_pattern = re.compile(r'(\d{1,3}\.){3,3}\d{1,3}')     #匹配ip地址
    sen_pattern = re.compile(r'<.*>')                       #匹配<发送者邮箱>
    blank_pattern= re.compile(r'^$')                        #匹配空行
    tag=0
    content=[]
    for i in f:
        if tag==0:
            if rec_pattern.match(i):
                ipstr=ip_pattern.search(i)
            if fro_pattern.match(i):
                senstr=sen_pattern.search(i)
            if blank_pattern.match(i):
                tag=1
        else:content.append(i)
        
    print("sender ip is:"+ipstr.group(0))
    print("sender is:"+senstr.group(0).strip('<>'))
    print("content is:")
    print(''.join(content))
            
      
        
        
