import subprocess
import os
import sys

class RecursiveGitPull:
    def __init__(self, Path):
        self.Path = Path

    def doGitPull(self):
        dirs = [f.name for f in os.scandir(self.Path) if f.is_dir()]
    
        SuccessList = []
        UpToDateList = []
        FailedList = []
        NotGitRepoList = []
        
       
        for dir in dirs:
            cmd = "cd " + os.path.join(Path,dir) + "&" + "git pull" 
                
            #print(cmd)

            try:
                result = subprocess.run(cmd, capture_output=True, shell=True)
                
                result_str = str(result.stdout.strip())
                err_str = str(result.stderr.strip())
                #print(result)
                if "Already up to date" in result_str:
                    UpToDateList.append(dir)
                elif "Updating" in result_str:
                    SuccessList.append(dir)
                elif "not a git repository" in err_str:
                    NotGitRepoList.append(dir)
            except subprocess.CalledProcessError as e:
                # Access the text output
                #print(result.stdout.strip())
                FailedList.append(dir)
                
        self.PrintFormattedFolderList("Success repo", SuccessList)
        self.PrintFormattedFolderList("Already up to date", UpToDateList)
        self.PrintFormattedFolderList("Failed repo", FailedList)
        self.PrintFormattedFolderList("Only Folders", NotGitRepoList)

    def PrintFormattedFolderList(self, Msg, List):
        print("-----------------------------------------------------")
        print("%s - %d" % (Msg, len(List)))
        print("-----------------------------------------------------")
        for i in range(0, len(List)):
            print("%s" % List[i])

    # def PrintFormattedFolderList(self, Msg, List):
        # print("-----------------------------------------------------")
        # print(Msg)
        # print("-----------------------------------------------------")
        # if len(List)<3:
            # for i in range(0, len(List)):
                # print("%s   " % List[i])
        # else:
            # for i in range(0,len(List)):
                # if i+2<len(List):
                    # print("%8s   %8s   %8s" % (List[i], List[i+1],List[i+2]))
                # elif i+1<len(List):
                    # print("%8s   %8s   %8s" % (List[i], List[i+1],List[i+2]))
                # i=i+2
        # print("-----------------------------------------------------")
            
if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: recursive_git_pull.py <path>")
        exit(0)
    else:
        Path = sys.argv[1]

        RecursiveGitPullObj = RecursiveGitPull(Path)
        
        RecursiveGitPullObj.doGitPull()