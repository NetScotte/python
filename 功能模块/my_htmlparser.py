from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self,tag,attrs):
        if tag == 'h3':
            if attrs=='event-title':
                self.tag=1
        if self.tag ==1 and tag=='a':
            self.tag=2  # 获取事件名的标记
        if self.tag ==2 and tag=='time':
            self.tag=3   # 获取时间的标记
        if self.tag==3:
            self.tag==4  # 获取地点的标记
        pass

    def handle_endtag(self,tag):
        pass

    def handle_startendtag(self,tag,attrs):
        pass

    def handle_data(self,data):
        if self.tag==2 and data != '':
            self.s['events']=data

        if self.tag==3:
            self.s['time']=data

        if self.tag==4:
            self.s['location']=data
            print(self.s)
            self.s={}
            self.tag=0

    def handle_comment(self,data):
        pass

    def handle_entityref(self,name):
        pass

    def handle_charref(self,name):
        pass


if __name__ =='__main__':
    with open('python_events.htm','r',encoding='utf-8') as f:
        html = f.read()

    parser = MyHTMLParser()
    parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
        
