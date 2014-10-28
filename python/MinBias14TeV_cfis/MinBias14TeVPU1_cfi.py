import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_12_1_RSv.root',
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_868_1_iA2.root',
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_825_1_EOm.root',
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_631_1_CZL.root',
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_225_1_dSt.root',
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_925_1_j61.root',
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_275_1_Byo.root',
         '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_18_1_uLb.root',
    )

)
