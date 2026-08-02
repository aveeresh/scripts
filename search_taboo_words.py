import os
import sys
import json

class SearchTabooWords:
       
    def __init__(self, SearchPath, JSONPath):
        self.SearchPath = SearchPath
        self.JSONPath = JSONPath

    def getTabooWordsList(self):
        try:
            with open(self.JSONPath, 'r', encoding='utf-8') as file:
                self.JSONData = json.load(file)
        except:
            print("[E] Unable to open %s file" % (self.JSONPath))
            exit(0)
        print("[I] Parsing %s file" % (self.JSONPath))
    
        return(self.JSONData["TabooWordsList"])
    
    def searchTabooWords(self):
        root = self.SearchPath
        
        TabooWordsList = self.getTabooWordsList()
        
        for path, subdirs, files in os.walk(root):
            for file in files:
                if (file.endswith(".c")) or (file.endswith(".h")):
                    f_handle = open( os.path.join(path,file), "r" )
                
                    try:
                        lines = f_handle.readlines()
                    
                        for line in lines:
                            for word in TabooWordsList:
                                if word in line:
                                    if "/*" not in line and "*" not in line:
                                        FileName = os.path.join(path,file)
                                        FileName = FileName.replace(self.SearchPath,"")
                                        print("[E] Found [%s] in [%s] - Line No. [%d]" % (word, FileName, lines.index(line)+1))
                                        break
                    except:
                        print("Cannot process file - %s" % (file))

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: search_taboo_words.py <SearchPath> <JSONFile>")
        exit(0)
    else:
        SearchPath = sys.argv[1]
        JSONPath = sys.argv[2]

        SearchTabooWordsObj = SearchTabooWords(SearchPath, JSONPath)
        
        SearchTabooWordsObj.searchTabooWords()