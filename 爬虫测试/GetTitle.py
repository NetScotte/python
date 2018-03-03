import re
import urllib.request as request

class GetTitle:
    def __init__(self):
        self.address = []
        self.html=[]
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
        self.header = {'User-Agent': user_agent}
        self.title_pattern = re.compile(r'<title>(.*)</title>')
        self.title=[]
        self.useadd=[]


    def getAddredd(self):
        with open('../data/address','r') as f:
            for i in f:
                self.address.append(i)

    def gethtml(self):
        count=0
        for i in self.address:
            count +=1
            try:
                print(count)
                req = request.Request('http://'+i, headers=self.header)
                with request.urlopen(req) as res:
                    self.html.append(res.read().decode('gbk',errors='ignore'))
                    self.useadd.append(i)
                    # with open('../data/myadd', 'a') as f:
                    #     f.write(i)
            except:
                continue
        return self.html

    def getTitList(self):
        for i in self.html:
            l = self.title_pattern.findall(i)
            if l:
                self.title.append(l)
                # with open('../data/mytitle', 'a') as f:
                #     f.write(l[0]+'  \n')

    def getTit(self):
        return self.title

    def getadd(self):
        return self.useadd


if __name__ == '__main__':
    mywork = GetTitle()
    mywork.getAddredd()
    mywork.gethtml()
    mywork.getTitList()
    title = mywork.getTit()
    add = mywork.getadd()


    for i in range(len(title)):
        try:
            with open('../data/myttile1','a') as f:
                f.write(title[i][0]+'  \n')

            with open('../data/myadd1','a') as f:
                f.write(add[i])
        except:
            continue

