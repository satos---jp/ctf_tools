#coding: utf-8
from socket import *
import time


#sudo gdb -q -p `pidof -s villager` -x gdbcmd
#socat TCP-L:10001,reuseaddr,fork EXEC:./villager

isgaibu = False
isgaibu = True

p = socket(AF_INET, SOCK_STREAM)
if isgaibu:
	p.connect(("ctfq.sweetduet.info", 10001))
	raw_input('gdb$')
	print p.recv(1024)
		
else:
	
	p.connect(("localhost", 10001))
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
		p.send(raw_input() + '\n')
		print p.recv(1024)




