import os
import sys

class CopyrightHdrChecker:
    def __init__(self, Path, CopyrightHdr):
        self.Path = Path
        self.CopyrightHdr = CopyrightHdr
        
    def checkHdrPresent(self):
        print("Checking for <%s>" % (self.CopyrightHdr))
        FilesWithoutHdr = []
        for root, dirs, files in os.walk(self.Path):
            for file in files:
                if file.endswith(".c") or file.endswith(".h") or file.endswith(".py"):
                    fp = open(os.path.join(root, file))
                    lines = fp.readlines()
                    #print(lines)
                    
                    HdrPresentFlag = False
                    for line in lines:
                        if self.CopyrightHdr in line:
                            HdrPresentFlag = True
                            break

                    if HdrPresentFlag==False:
                        FilesWithoutHdr.append(os.path.join(root, file))

        return(FilesWithoutHdr)
        
if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: check_copyright_header.py <path> <header_string>")
        exit(0)
        
    path = sys.argv[1]
    hdr = sys.argv[2]
    CopyrightHdrCheckerObj = CopyrightHdrChecker(path, hdr)
    FileList = CopyrightHdrCheckerObj.checkHdrPresent();
    
    if len(FileList)!=0:
        print("No. of files with missing header = %d\n" % len(FileList))
        
        for File in FileList:
            print(File)
            print("-----------------------------------------------------------------------------------------------------------------")
        