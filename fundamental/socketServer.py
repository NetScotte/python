import socket

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

socketServer.bind((host, port))

socketServer.listen(5)

while True:
    socketClient, addr = socketServer.accept()

    print("连接地址:%s" % str(addr))

    msg = '欢迎访问我的服务器'
    socketClient.send(msg.encode('gbk'))
    socketClient.close()
