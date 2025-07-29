import os
import re
import shutil

replacement_spaces = ' '*4
def getListOfFiles(dirName):
	listOfFile = os.listdir(dirName)
	allFiles = list()
	for entry in listOfFile:
		fullPath = os.path.join(dirName, entry)		   
		if os.path.isdir(fullPath):
			allFiles = allFiles + getListOfFiles(fullPath)
		else:
			if fullPath.endswith(".c") or fullPath.endswith(".h"):
				  allFiles.append(fullPath) 
	return allFiles
	
def Tab_Space(Files):
	for File in Files:
		inputFile = open(File, 'r') 
		exportFile = open("tabs.replaced", 'w')
		for line in inputFile:
			new_line = line.replace('\t', replacement_spaces)
			exportFile.write(new_line) 

		inputFile.close()
		exportFile.close()
		shutil.copyfile("tabs.replaced", File)
		os.remove("tabs.replaced")
	print("De-Tabbing Completed")
	
if __name__ == "__main__":
	Files = []
	root = os.getcwd()
	print( 'Searching for files with tabs' )
	Files = getListOfFiles(root)
	Tab_Space(Files)
