import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_827_1_O0D.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_103_1_qHK.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_566_1_W2B.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_930_1_xGX.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_806_1_UQz.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_54_1_ZBp.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_388_1_Yj8.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_945_1_0fu.root',
    )

)
