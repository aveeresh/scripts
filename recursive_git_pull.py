import subprocess
import os
import sys

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: recursive_git_pull.py <path>")
        exit(0)
    else:
        Path = sys.argv[1]
        
    dirs = [f.name for f in os.scandir(Path) if f.is_dir()]
   
    for dir in dirs:
        cmd = "cd " + os.path.join(Path,dir) + "&" + "git pull" 
            
        #print(cmd)

        try:
            result = subprocess.run(cmd, capture_output=True, shell=True)
        except subprocess.CalledProcessError as e:
            # Access the text output
            print(result.stdout.strip())
