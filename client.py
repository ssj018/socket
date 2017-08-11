#!/usr/bin/python
#-- coding:UTF-8 --

import socket
import sys
import time

def colors_print():
  print 'Error code:' + '\033[1;32;40m' +str(msg[0])+'\033[0m Error message:'+ '\033[1;31;40m' + msg[1] + '\033[0m'


try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
  print 'Failed to create socket.'
  colors_print()
  sys.exit();
else:
  print 'Socket has been created !'

#time.sleep(10)

#host = '115.239.241.112'
host='127.0.0.1'
port = 9999

try:
  s.connect((host,port))
  print 'connected to ' +host
except socket.error,msg:
  print 'could not connect to'+ host
  colors_print()
  sys.exit();

#time.sleep(10)

#message = "GET / HTTP/1.1\r\n\r\n"
#try:
#  s.sendall(message)
#except socket.error:
#  print 'Send failed' 
#  sys.exit()
#
reply = s.recv(4096)
#time.sleep(20)
print reply
#time.sleep(10)
s.close()

