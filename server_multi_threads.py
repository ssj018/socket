#!/usr/bin/python
#--coding:UTF-8 --

import socket
import sys
import time
import thread
import logging

logging.basicConfig(level=logging.INFO)

def do_with_connect():
  try:
    logging.info('链接地址'+str(addr))
    c.send('welcome to mds')
    time.sleep(20)
    c.close()
  except socket.error,msg:
    #print 'Error code:' + '\033[1;32;40m' +str(msg[0])+'\033[0m Error message:'+ '\033[1;31;40m' + msg[1] + '\033[0m'
    logging.error('send error:'+str(msg))
try:
  s=socket.socket()
except socket.error,msg:
  logging.erro('\033[1;32;40m create socket failed:\033[m'+str(msg))
  sys.exit()
else:
  logging.info("the socket has been created")

host='127.0.0.1'
port=9999
try:
  s.bind((host,port))
  s.listen(5)
  logging.info('start to  listen no  port 9999')
except socket.error,msg:
  logging.error(msg)
  sys.exit()
#else:
#  print "server has been start!"

while True:
#  thread.start_new(do_with_connect,())
  c , addr = s.accept()
  try:
    thread.start_new_thread(do_with_connect,())
  except thread.error,msg:
    logging.error('threads error:'+str(msg))
