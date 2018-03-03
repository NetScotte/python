import socket

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
socketClient.connect((host, port))

msg = socketClient.recv(1024)

print(msg.decode('gbk'))
socketClient.close()
