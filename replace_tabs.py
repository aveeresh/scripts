import os

root = os.getcwd()

for path, subdirs, files in os.walk(root):
	for file in files:
		if (file.endswith(".c")) or (file.endswith(".h")):
			f_handle = open( os.path.join(path,file), "r" )
			lines = f_handle.readlines()
			
			counter = 0
			for line in lines:
				if ((line.find("\t",0, len(line))>-1)):
					lines[counter] = line.replace( "\t", "    " )
				counter += 1
			
			#close file and re-open in write mode
			f_handle.close()
			
			f_handle = open( os.path.join(path,file), "w" )
			
			for line in lines:
				f_handle.write( line )
			
			f_handle.close()

