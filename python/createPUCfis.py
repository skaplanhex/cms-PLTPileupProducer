#makes input cfi files for all pileup scenarios!

def numEventsNeeded(nPU):
    return 15000*nPU

from fileRegister import MinBias14TeV_NoSmear #import the file assignments for each PU scenario
from numpy import random
# puDict={
# 1:pu1,
# 2:pu2,
# 3:pu3,
# 5:pu5,
# 10:pu10,
# 15:pu15,
# 20:pu20,
# 30:pu30,
# 40:pu40
# }
PUs = [1,2,3,5,10,15,20,30,40,0]
EVENTSPERFILE=2000
files = MinBias14TeV_NoSmear[:]
# add quotes and commas because I forgot to do it earlier
filesnew=[]
for f in files:
    filesnew.append("'"+f+"',")
files = filesnew

for pu in PUs:
    numNeeded = numEventsNeeded(pu)
    numAdded = 0
    pustr = ""
    if pu == 0:
        pustr += "Actual"
    else:
        pustr += "PU%i"%pu
    out = open("MinBias14TeV_NoSmear%s_cfi.py"%pustr,'w')
    out.write("import FWCore.ParameterSet.Config as cms\n")
    out.write("\n")
    out.write('source = cms.Source("PoolSource",\n')
    out.write("    fileNames = cms.untracked.vstring(\n")
    if pu != 0:
        while (numAdded < numNeeded):
            num = random.randint( len(files) )
            f = files.pop(num)
            out.write("         "+f+"\n")
            numAdded += 2000
    else:
        for f in files:
            out.write(f+"\n")
    out.write("    )\n")
    out.write("\n")
    out.write(")\n")
    out.close()
print "cfi files made! Here are the files we haven't used yet:"
for f in files:
    print f

