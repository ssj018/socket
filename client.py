#!/usr/bin/python
#-- coding:UTF-8 --

import socket
import sys
import time

try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
  print 'Failed to create socket. Error code' + str(msg[0]) + ', Error message:' + mds[1]
  sys.exit();
else:
  print 'Socket has been created !'

#time.sleep(10)

host = '115.239.211.112'
port = 80 

try:
  s.connect((host,port))
  print 'connected to ' +host
except socket.error:
  print 'could not connect to'+host
  sys.exit();

#time.sleep(10)

message = "GET / HTTP/1.1\r\n\r\n"
try:
  s.sendall(message)
except socket.error:
  print 'Send failed' 
  sys.exit()

reply = s.recv(4096)
print reply
#time.sleep(10)
s.close()

