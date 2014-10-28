#makes input cfi files for all beamspot scenarios!

import os, sys

eospath = "/eos/uscms/store/user/skaplan/noreplica/MinBias14TeV/"
shortpath = "/store/user/skaplan/noreplica/MinBias14TeV/"

outfiles = os.listdir(eospath)
outfilesnew=[]
for f in outfiles:
	outfilesnew.append("		'"+shortpath + f + "',")
out = open("MinBias14TeV_cfi.py",'w')
out.write("import FWCore.ParameterSet.Config as cms\n")
out.write("\n")
out.write('source = cms.Source("PoolSource",\n')
out.write("	fileNames = cms.untracked.vstring(\n")
counter = 0
for f in outfilesnew:
	counter += 1
	if (counter % 220 == 0):
		out.write(f+")+cms.untracked.vstring(\n")
	else:
		out.write(f+"\n")
out.write("	)\n")
out.write("\n")
out.write(")\n")
out.close()
