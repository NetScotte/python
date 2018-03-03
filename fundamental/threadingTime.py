import threading
import time

class myThread(threading.Thread ):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程："+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,5)
        threadLock.release()
        print("退出线程:"+self.name)

def print_time(threadName , delay,counter):
    while counter:
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime (time.time ())))
        counter -=1
        
threadLock = threading.Lock()
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

thread1.start()
thread2.start()
#如果没有thread1.join(),主线程会继续运行，执行print , join可理解阻塞主线程
thread1.join()
thread2.join()
print("退出主进程")
