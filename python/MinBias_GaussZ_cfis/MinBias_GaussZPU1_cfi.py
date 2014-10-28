import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
         '/store/user/skaplan/noreplica/MinBias_GaussZ/outfile14TeVSKIM_407_1_6d8.root',
         '/store/user/skaplan/noreplica/MinBias_GaussZ/outfile14TeVSKIM_282_1_JCE.root',
         '/store/user/skaplan/noreplica/MinBias_GaussZ/outfile14TeVSKIM_347_1_C8r.root',
         '/store/user/skaplan/noreplica/MinBias_GaussZ/outfile14TeVSKIM_553_1_n2X.root',
         '/store/user/skaplan/noreplica/MinBias_GaussZ/outfile14TeVSKIM_218_1_c8d.root',
         '/store/user/skaplan/noreplica/MinBias_GaussZ/outfile14TeVSKIM_672_1_Boo.root',
    )

)
