
class test:
    
    def first(self):
        i=3
        print(self.recursive(i))
    
    def recursive(self,i):
        s=0;
        if i==0:
            return 1
        else:
            s = i*self.recursive(i-1)
        return s

class test1:
    def first(self,n=3):
        word=''
        with open('./allword','a') as f2:
            self.recursive(f2,word,n)
                
    def recursive(self,f2,word,n):
        if n<=1:
            with open('./name','r') as f1:
                for i in f1:
                    f2.write(word+i.strip()+'\n')
                return 1
        with open('./name','r') as f:
            for j in f:
                self.recursive(f2,word+j.strip(),n-1)
        

if __name__=='__main__':
    t=test1()
    t.first()
