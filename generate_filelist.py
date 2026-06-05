import os
import sys

class Generate_FileList:
    def __init__(self, Path, FilterString):
        self.Path = Path
        self.FilterString = FilterString
        self.LOGFILE = "filelist.txt"
        
    def generateFileList(self):
        Filters = self.generateFilterList()
        
        FileList = []
        for root, dirs, files in os.walk(self.Path):
            for file in files:
                for Filter in Filters:
                    if file.endswith(Filter):
                        String = root+"\\"+file
                        String = String.replace(self.Path,"")
                        FileList.append(String)
        
        self.writeFileListToFile(FileList)

    def generateFilterList(self):
        Filters = self.FilterString.split(",")
        for i in range(0, len(Filters)):
            Filters[i] = Filters[i][1:len(Filters[i])]
        
        return(Filters)
                        
    def writeFileListToFile(self, FileList):
        with open(self.LOGFILE,"w") as f:
            for File in FileList:
                f.write(File+"\n")

                        
if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: generate_filelist.py <path> <comma_separated_file_extensions>")
        exit(0)
        
    path = sys.argv[1]
    filter_string = sys.argv[2]
    Generate_FileListObj = Generate_FileList(path, filter_string)
    FileList = Generate_FileListObj.generateFileList()
    
    print("[I] File list generated!")
    
                        
                        
 