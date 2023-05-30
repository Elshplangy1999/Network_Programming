from socket import *

S = socket (AF_INET, SOCK_STREAM)
S.connect(("127.0.0.1",1025))

time = S.recv(2048)
time = time.decode()

print('Time from server is : ',time)