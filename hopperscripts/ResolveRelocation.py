print('-' * 60 + 'BEGIN' + '-' * 60)

doc = Document.getCurrentDocument()
#print(dir(doc))
#assert False
fpath = doc.getExecutableFilePath()
print('file',fpath)

import os
import subprocess
os.environ["LANG"] = "C"
syms = subprocess.check_output(['readelf',fpath,'-r'])
syms = syms.split('\n')[3:]
syms = map(lambda x: filter(lambda d: d!='',x.split(' ')),syms)
syms = filter(lambda x: len(x)>=6,syms)
syms = map(lambda x: (int(x[0],16),x[-3]),syms)
syms = dict(syms)
print(syms)

entrp = doc.getEntryPoint()
codeseg = None
for i in range(doc.getSegmentCount()):
	seg = doc.getSegment(i)
	stp = seg.getStartingAddress()
	enp = stp + seg.getLength()
	print('segname:',seg.getName())
	if stp <= entrp and entrp < enp:
		codeseg = seg
		break
seg = None
assert codeseg is not None

def isproc(p):
	return codeseg.getTypeAtAddress(np) is Segment.TYPE_PROCEDURE

for np in range(codeseg.getStartingAddress(),codeseg.getStartingAddress() + codeseg.getLength()):
	#print('np',hex(np),'type:',Segment.stringForType(codeseg.getTypeAtAddress(np)))
	#print(codeseg.getNameAtAddress(np))
	if not isproc(np):
		continue
	ins = codeseg.getInstructionAtAddress(np)
	if not ins.isAnInconditionalJump():
		continue
	refs = codeseg.getReferencesOfAddress(np)
	refs = filter(lambda p: isproc(p),refs)
	refs = filter(lambda p: codeseg.getInstructionAtAddress(p).getInstructionString() == 'call',refs)	
	if len(refs) == 0:
		continue
	
	inst = codeseg.getInstructionAtAddress(np)
	assert inst.getInstructionString() == 'jmp'
	pad = inst.getRawArgument(0)
	assert pad[:3]=='[0x' and pad[-1]==']'
	pad = int(pad[3:-1],16)
	pfn = syms[pad]
	doc.setNameAtAddress(np,'jj_' + pfn)
	continue
	
	print(hex(np),hex(pad))
	for p in refs:
		if not isproc(p):
			continue
		codeseg.setInlineCommentAtAddress(p,'lib: ' + pfn)
	#print('isjmp',hex(np))
	#print('refs',refs)
	#print(hex(np))
	# np = codeseg.getNextAddressWithType(np,Segment.TYPE_PROCEDURE)

