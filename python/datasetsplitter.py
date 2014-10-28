import os
directory = "/eos/uscms/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/"
shortpath = "/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/"
outfiles = os.listdir(directory)
PUs = [1,2,3,5,10,15,20,25,30,35,40]
puDict={}
for pu in PUs:
    numFiles = 5*pu
    files = []
    for i in range(numFiles):
        fName = outfiles.pop()
        files.append(fName)
    puDict[pu] = files

for pu in PUs:
    print "#########PU = %i"%pu
    print " "
    for f in puDict[pu]:
        print "'"+shortpath+f+"',"
    print " "

print "#####Actual Events!"
for f in outfiles:
    print "'"+shortpath+f+",'"