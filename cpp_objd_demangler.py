import os

def dem(s):
	os.system('echo "' + s + '" | c++filt > do.txt')
	with open('do.txt','r') as fp:
		res = fp.readlines()[0].split('\n')[0]
	#print res
	return res
	


with open('objd.txt','r') as fp:
	gs = ''.join(fp.readlines())
	ls = len(gs)
	ts = ""
	i = 0
	while i<ls:
		if gs[i]!='<':
			ts += gs[i]
			i += 1
		else:
			ts += gs[i]
			i += 1
			cs = ""
			while gs[i]!='>' and gs[i] != '@':
				cs += gs[i]
				i += 1
			ts += dem(cs)
			#print ts
	with open('demd.txt','w') as gp:
		gp.write(ts)


			
		
