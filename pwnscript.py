#coding: utf-8
from socket import *
import time


#sudo gdb -q -p `pidof -s execfile` -x gdbcmd
#socat TCP-L:10001,reuseaddr,fork EXEC:./execfile

#./../../tools/rp-lin-x86 -file=mylibc --rop=3 --unique > mygads.txt


isgaibu = False
isgaibu = True

sock = socket(AF_INET, SOCK_STREAM)
if isgaibu:
	sock.connect(("gaibu.sa-ba-", 10001))
	raw_input('gdb$')
		
else:
	sock.connect(("localhost", 10001))
	raw_input('gdb$')


def addr2s(x):
	res = ""
	for i in xrange(4):
		res += chr(x % 256)
		x /= 256
	return res

def s2hex(s):
	return map(lambda c: hex(ord(c)),s)
	
def s2addr(s):
	res = 0
	for i in xrange(4):
		res *= 256
		res += ord(s[3-i])
	return res
	
def shell():
	while True:
		sock.send(raw_input() + '\n')
		print sock.recv(1024)

def getunt(c):
	res = ""
	while res=='' or res[-len(c):]!=c:
		res += sock.recv(1)
		#print res
	print res
	return res

def send(s):
	#print '[sending :: %s]' % s
	sock.send(s)

def getshellc(fn):
	res = ""
	with open(fn,'rb') as fp:
		res = fp.read()
	print map(ord,res)
	return res


