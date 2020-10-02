#this can be used to find files which have a word hidden in them
import os
fileformat=input("fileformat you want to find the word in")#file format to find the word in
wordtobefound=input("what word do you want to find in this folder's files")#word which you want to find
def wordfinder(filename):
    with open(filename, "r") as f:
        filecontent = f.read()
        #.lower written below because the word may be like this heLlO
    if wordtobefound in filecontent.lower():
        return True
    else:
        return False
dir_contents= os.listdir()
print(dir_contents)
nwordtobefound=0
for item in dir_contents:
    if item.endswith(fileformat):
        print(f"detecting {wordtobefound} in {item}")
        flag = wordfinder(item)
        if(flag):
                nwordtobefound=nwordtobefound+1
                print(f"{wordtobefound} found in {item}")
        else:
            print(f"{wordtobefound} not found in {item}")
print("wordfinder summary")
print(f"{nwordtobefound} files found with {wordtobefound} hidden into them")
input()
