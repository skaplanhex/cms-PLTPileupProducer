import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_170_1_JEx.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_20_1_9t5.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_573_1_ZCK.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_227_1_eoN.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_939_1_DIS.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_18_1_pwz.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_460_1_Gct.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_47_1_UuC.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_411_1_b5m.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_922_1_Ad5.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_16_1_nx7.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_553_1_DfX.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_457_1_XbL.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_459_1_DTr.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_552_1_kPs.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_29_1_uJX.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_533_1_dGH.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_43_1_pvg.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_794_1_9Ob.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_417_1_phq.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_887_1_bkQ.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_618_1_rSr.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_769_1_8SS.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_508_1_n2W.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_760_1_aEM.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_941_1_Ha1.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_835_1_4h9.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_154_1_QEI.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_505_1_ta2.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_171_1_2Y6.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_917_1_pLA.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_780_1_Nmk.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_392_1_8qP.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_802_1_OVo.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_203_1_dvN.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_276_1_H9X.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_879_1_tlV.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_40_1_WwJ.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_84_1_tkE.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_367_1_OZQ.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_804_1_nCC.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_424_1_7vU.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_869_1_RTU.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_422_1_GSB.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_973_1_sIQ.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_223_1_V0a.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_703_1_Dxr.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_211_1_leO.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_842_1_uZx.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_117_1_81I.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_450_1_i8F.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_512_1_gwZ.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_768_1_5GR.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_586_1_uLL.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_563_1_5UL.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_720_1_3Oe.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_85_1_sGL.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_559_1_yEb.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_831_1_TwX.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_621_1_nW3.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_569_1_W2E.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_189_1_8xu.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_348_1_9Sa.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_237_1_r9q.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_363_1_Vyn.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_183_1_pCC.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_271_1_to0.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_754_1_9vL.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_938_1_lfU.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_265_1_oT0.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_2_1_fCA.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_650_1_fbs.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_23_1_VB4.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_181_1_ZCu.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_636_1_XEQ.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_998_1_hJe.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_514_1_6x4.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_100_1_LKc.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_96_1_qnW.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_95_1_od2.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_143_1_O5n.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_162_1_bJz.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_434_1_Kdg.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_77_1_cjy.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_182_1_vne.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_609_1_Fhv.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_195_1_QTf.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_484_1_IHe.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_521_1_jxX.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_867_1_G9M.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_414_1_U2B.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_90_1_Z1i.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_37_1_VOn.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_353_1_NQx.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_273_1_xgx.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_974_1_v2a.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_882_1_Pyj.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_65_1_0fP.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_604_1_ZSU.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_464_1_60D.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_479_1_16b.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_75_1_b0t.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_834_1_dN6.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_690_1_FrS.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_135_1_O3a.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_93_1_ss8.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_709_1_qa0.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_310_1_WMo.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_254_1_890.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_864_1_QNE.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_810_1_0gJ.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_617_1_uCg.root',
         '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_62_1_nUg.root',
    )

)
