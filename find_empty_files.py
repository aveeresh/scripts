import os
import sys

root = os.getcwd()

for path, subdirs, files in os.walk(root):
	for file in files:
		size = os.path.getsize(os.path.join(path,file))
		if( len(sys.argv)==1 ):
			if( size==0 ):
				print( os.path.join(path,file) )
				break
		else: 
			if(size==0 and file.endswith("."+sys.argv[1])):
				print( os.path.join(path,file) )
				break
