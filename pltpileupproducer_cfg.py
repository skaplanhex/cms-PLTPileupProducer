from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "pileuptree.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "Name of output file"
)
options.register('threshold',
                 4000,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.int,
                 "electron threshold for writing hit to digi output"
)
options.register('inputCfi',
                'DUMMY',
                VarParsing.multiplicity.singleton,
                VarParsing.varType.string,
                "which cfi if any to pass as input"
)
options.register('reportEvery', 10,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report every N events (default is N=10)"
)
## 'maxEvents' and 'outputFile' are already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)
options.parseArguments()



import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

#source files

#if cfi file passed in at runtime, use it as input
if options.inputCfi != "DUMMY":
    process.load("Analyzers.PLTPileupProducer."+options.inputCfi)
#if no file is passed in at runtime, use this as the input
else:
    process.source = cms.Source("PoolSource",
            fileNames = cms.untracked.vstring(
                #"file:/uscms_data/d3/skaplan/PLT/sim/CMSSW_7_1_0_pre4/src/outfile14TeV.root"
                #'/store/user/skaplan/MinBiasBeamSpotPhi0R0/outfile14TeV_18_1_OfZ.root'
                # '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_313_1_qk7.root'
                "/store/user/skaplan/noreplica/MinBias_WithSimTracks/outfile14TeVSKIM_33_1_oLh.root"
            )
    )
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.TFileService = cms.Service("TFileService",
        fileName = cms.string(options.outfilename)
)

#maybe have these paramateters as ones that can be passed in via VarParsing?
process.produce = cms.EDAnalyzer('PLTPileupProducer')

process.p = cms.Path(process.produce)
