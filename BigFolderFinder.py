import humanize
import os
import time
import pandas as pd

path = ""


while True:
    path = input("Input the path to scan:\n")
    is_it = os.path.isdir(path)
    if is_it == True:
        break
    else:
        print("Folder not found (maybe folder is a file) here is an example ""D:\\ExampleFolderD\\examplefolder2\\"" or ""C:/yetanotherexample/folder/""")

data = {
    "Folders":[],
    "Sizes":[],
    "Bites":[]
}

files = os.listdir(path)

path = path + "/"

print("It's doing something")

for folder in files:  
    size = 0
    tempsize = 0
    path2 = path + folder + "/"
    isdir = os.path.isdir(path + folder)

    if isdir == True: 
        for root, dirs, subfiles in os.walk(path + folder, topdown=True):
            for name in subfiles:
                name = os.path.join(root, name)
                filesize = 0
                filesize =  os.path.getsize(name)
                tempsize += filesize
        data["Folders"].append(folder)
        data["Bites"].append(tempsize)
        size = humanize.naturalsize(tempsize)
        data["Sizes"].append(size)

resultsun = pd.DataFrame(data)

results = resultsun.sort_values(by="Bites", ascending=False)

with pd.option_context('display.max_rows', None,
'display.max_columns', None,
'display.precision', 3,
):
    print(results.to_markdown())


input("press enter to exit")