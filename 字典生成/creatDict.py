import itertools

class MyDict:
    def __init__(self):
        self.name=[]
        self.word=[]
        self.adj=[]
        self.Dict=[]
        self.fileName=['name','word','adj']

    def createList(self):
            with open('./name','r') as f1:
                for line in f1:
                    self.name.append(line.strip())
            with open('./word','r') as f2:
                for line in f2:
                    self.word.append(line.strip())
            with open('./adj','r') as f3:
                for line in f3:
                    self.adj.append(line.strip())

            print(self.name)
            print(self.word)
            print(self.adj)

    # 一般密码为姓名，短语，这两者可以来自词典，
    # 然后就是人称代词/姓名等+代词/动词/介词+短语
    # 此处只负责产生短语，其他来自收集
    def produceSentence(self):
        with open('./sentence','a') as f:
            for w1 in self.name:
                for w2 in self.adj:
                    for w3 in self.word:
                        sentence = w1+w2+w3+'\n'
                        f.write(sentence)

    def allWord(self,fileName='name',num=4):
        filePath = r'./'+fileName
        word=''
        with open(filePath,'r') as f1:
            with open('./allWord','a') as f2:
                self.doround(f1,word,num--)
                

    def doround(self,f,word,num):
        
                
                
            

    def work(self):
        self.createList()
        self.produceSentence()
        

if __name__=='__main__':
    Dict=MyDict()
    Dict.work()
