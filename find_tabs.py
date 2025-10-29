import os

root = os.getcwd()

for path, subdirs, files in os.walk(root):
	for file in files:
		if (file.endswith(".c")) or (file.endswith(".h")):
			f_handle = open( os.path.join(path,file), "r" )
			try:
				lines = f_handle.readlines()

				for line in lines:
					if line.find("\t",0, len(line))!=-1:
						print( os.path.join(path,file) )
						break
			except:
				print("Cannot process file - %s" % (file))


