import os
import sys, argparse
import random
parsers = argparse.ArgumentParser()
parsers.add_argument("-i", "--index", help="Please enter begin index")
parsers.add_argument("-f", "--folder", help="Please enter folder path")
args = parsers.parse_args()
def changeFileName(oldName, newName):
    os.rename(oldName, newName)

def changeAllFileName(beginIndex, folder):
    for file in os.listdir(folder):
        
        changeFileName(folder + '/' + file, folder + '/' + str(beginIndex) + '.gif')
        beginIndex = int(beginIndex)+1
def changeAllFileNameSuffer(endIndex, folder):
    listIndices = list(range(0, int(endIndex)))
    print(listIndices)
    random.shuffle(listIndices)
    i = 0
    for file in os.listdir(folder):
        changeFileName(folder + '/' + file, folder + '/' + str(listIndices[i]) + '.gif')
        i = i + 1

changeAllFileNameSuffer(args.index, args.folder)
print(args.index)
print(args.folder)