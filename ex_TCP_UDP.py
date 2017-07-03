import socket
import threading
import time


def client():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('www.sina.com.cn', 80))

    s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    buffer = []
    while True:

        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = ''.join(buffer)

    s.close()

    header, html = data.split('\r\n\r\n', 1)
    print header

    with open('sina.html', 'wb') as f:
        f.write(html)

def client2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print s.recv(1024)
    for data in ['Michael', 'Tracy', 'Sarah']:
        # 发送数据:
        s.send(data)
        print s.recv(1024)
    s.send('exit')
    s.close()

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print ("waiting for connection!!!")

    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()




if __name__ == '__main__':
    server()