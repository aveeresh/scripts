import os

root = os.getcwd()

#print("Parsing all files under <%s>" % (root) )

for path, subdirs, files in os.walk(root):
	for file in files:
		if (file.endswith(".c")) or (file.endswith(".h")):
			#print("Parsing %s" % (file) )
			f_handle = open( os.path.join(path,file), "r" )
			lines = f_handle.readlines()
			
			for line in lines:
				#print(line)
				#print("End char = %s" % ("SPACE" if line[len(line)-2]==" " else "NOT SPACE"))
				if (line[len(line)-2]==" "):
					print( os.path.join(path,file) )
					break
