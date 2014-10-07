// -*- C++ -*-
//
// Package:    Analyzers/PLTPileupProducer
// Class:      PLTPileupProducer
// 
/**\class PLTPileupProducer PLTPileupProducer.cc Analyzers/PLTPileupProducer/plugins/PLTPileupProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  steven kaplan
//         Created:  Mon, 29 Sep 2014 16:22:11 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//PSimHitContainer includes PSimHit and Vector already
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "SimDataFormats/Track/interface/SimTrack.h"

#include "SimDataFormats/Vertex/interface/SimVertex.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "DataFormats/GeometryVector/interface/LocalVector.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "TTree.h"

#include <math.h>
#include <map>
#include <string>
#include <sstream>
#include <vector>
#include <tuple>
#include <cstdlib>
#include <fstream>
//for split()
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>

using namespace edm;
using namespace std;
//
// class declaration
//

class PLTPileupProducer : public edm::EDAnalyzer {
   public:
      explicit PLTPileupProducer(const edm::ParameterSet&);
      ~PLTPileupProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual int getChannel(int,int,int);
      virtual tuple<int,int,int,int,int,int> analyzeDetId(int);
      virtual int getADC(double);
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      edm::Service<TFileService> fs;
      TTree* tree;
      int eventCounter;
      int nHits;
      int eventNum;
      vector<float> pabs;
      vector<float> energyLoss;
      vector<float> thetaAtEntry;
      vector<float> phiAtEntry;
      vector<float> tof;
      vector<int> particleType;
      vector<int> detUnitId;
      vector<int> trackId;
      vector<int> channel;
      vector<int> roc;
      vector<int> column;
      vector<int> row;
      vector<int> adc;


      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
PLTPileupProducer::PLTPileupProducer(const edm::ParameterSet& iConfig)

{
    //now do what ever initialization is needed
    eventCounter = 0;

    tree = fs->make<TTree>("tree","tree");
    tree->Branch("eventNum",&eventNum,"eventNum/I");
    tree->Branch("nHits",&nHits,"nHits/I");
    tree->Branch("pabs",&pabs);
    tree->Branch("energyLoss",&energyLoss);
    tree->Branch("thetaAtEntry",&thetaAtEntry);
    tree->Branch("phiAtEntry",&phiAtEntry);
    tree->Branch("tof",&tof);
    tree->Branch("particleType",&particleType);
    tree->Branch("detUnitId",&detUnitId);
    tree->Branch("trackId",&trackId);
    tree->Branch("channel",&channel);
    tree->Branch("roc",&roc);
    tree->Branch("column",&column);
    tree->Branch("row",&row);
    tree->Branch("adc",&adc);

}


PLTPileupProducer::~PLTPileupProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}
int
PLTPileupProducer::getChannel(int pltNum, int halfCarriageNum, int telNum){
    int channelNum = -1;
    if(pltNum == 0){
        if(halfCarriageNum == 0){
            switch(telNum){
                case 0:
                    channelNum = 1;
                    break;
                case 1:
                    channelNum = 2;
                    break;
                case 2:
                    channelNum = 3;
                    break;
                case 3:
                    channelNum = 4;
                    break;
            }
        }
        else{
            switch(telNum){
                case 0:
                    channelNum = 5;
                    break;
                case 1:
                    channelNum = 6;
                    break;
                case 2:
                    channelNum = 7;
                    break;
                case 3:
                    channelNum = 8;
                    break;
            }
        }
    }
    else{
        if(halfCarriageNum == 0){
            switch(telNum){
                case 0:
                    channelNum = 9;
                    break;
                case 1:
                    channelNum = 10;
                    break;
                case 2:
                    channelNum = 11;
                    break;
                case 3:
                    channelNum = 12;
                    break;
            }
        }
        else{
            switch(telNum){
                case 0:
                    channelNum = 13;
                    break;
                case 1:
                    channelNum = 14;
                    break;
                case 2:
                    channelNum = 15;
                    break;
                case 3:
                    channelNum = 16;
                    break;
            }
        }
    }
    return channelNum;
}


tuple<int,int,int,int,int,int>
PLTPileupProducer::analyzeDetId(int detid){
    std::stringstream ss;
    ss << detid;
    std::string detidstring = ss.str();
    int detidsize = detidstring.size();
    //since many identifiers can be zero, the size of the integer can vary! Need to switch on all possible sizes to determine the identifiers from the detid.
    
    //There needs to be a more elegant way to do this...
    int pltNo = -1;
    int halfCarriageNo = -1;
    int telNo = -1;
    int planeNo = -1;
    int rowNo = -1;
    int columnNo = -1;
    
    if (detidsize == 1 || detidsize == 2) {
        pltNo = 0;
        halfCarriageNo = 0;
        telNo = 0;
        planeNo = 0;
        rowNo = 0;
        columnNo = detid;
    }
    else if (detidsize == 3 || detidsize == 4){
        pltNo = 0;
        halfCarriageNo = 0;
        telNo = 0;
        planeNo = 0;
        rowNo = (detid - (detid % 100))/100;
        columnNo = detid % 100;
    }
    else if (detidsize == 5){
        pltNo = 0;
        halfCarriageNo = 0;
        telNo = 0;
        planeNo = (detid - (detid % 10000))/10000;
        rowNo = ((detid % 10000)-(detid % 100))/100;
        columnNo = detid % 100;
    }
    else if (detidsize == 6){
        pltNo = 0;
        halfCarriageNo = 0;
        telNo = (detid - (detid % 100000))/100000;
        planeNo = ((detid - (100000*telNo)) - (detid % 10000))/10000;
        rowNo = ((detid % 10000)-(detid % 100))/100;
        columnNo = detid % 100;
    }
    else if (detidsize == 7){
        pltNo = 0;
        halfCarriageNo = (detid - (detid % 1000000))/1000000;
        telNo = ((detid - (1000000*halfCarriageNo)) - (detid % 100000))/100000;
        planeNo = (detid-(1000000*halfCarriageNo)-(100000*telNo)-(detid % 10000))/10000;
        rowNo = ((detid % 10000)-(detid % 100))/100;
        columnNo = detid % 100;
    }
    else if (detidsize == 8){
        int temp [8];
        //fill array with digits in detid and use the array for the various ids
        for(int i =0; i<8; i++){
            char aChar = detidstring.at(i);
            int anInt = atoi(&aChar); //convert char to int
            temp[i] = anInt;
        }
        pltNo = temp[0];
        halfCarriageNo = temp[1];
        telNo = temp[2];
        planeNo = temp[3];
        rowNo = 10*temp[4]+temp[5];
        columnNo = 10*temp[6]+temp[7];
    }
    else{
        std::cout << "DETID = " << detid << " NOT EXPECTED!! INVESTIGATE!!" << std::endl;
    }
    if (pltNo == -1 || halfCarriageNo == -1 || telNo == -1 || planeNo == -1 || rowNo == -1 || columnNo == -1) {
        std::cout << "ONE OF THE ELEMENTS WEREN'T SET CORRECTLY FOR DETID = " << detid << ". INVESTIGATE!!!" << std::endl;
    }
    return make_tuple(pltNo,halfCarriageNo,telNo,planeNo,rowNo,columnNo);
}
int
PLTPileupProducer::getADC(double eLoss){
    double numberOfElectrons = ( (eLoss*(1e9))/3.6 ); //convert to eV then to electrons

    //to get adc, use GainCal coefficient of 1.538462e-2 and round to nearest int
    const double GAINCAL = 1.538462e-2;
    int tempadc = round( numberOfElectrons*GAINCAL );
    return tempadc;
}


//
// member functions
//

// ------------ method called for each event  ------------
void
PLTPileupProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    eventNum = (int)iEvent.id().event();
    eventCounter++;

    edm::Handle<PSimHitContainer> simHitHandle;
    edm::InputTag tag("g4SimHits","PLTHits","SIM");
    iEvent.getByLabel(tag,simHitHandle);
    nHits = simHitHandle->size();

    for (int iHit = 0; iHit < (int)simHitHandle->size(); iHit++){
        PSimHit hit = simHitHandle->at(iHit);

        int detid = hit.detUnitId();

        pabs.push_back( hit.pabs() );
        energyLoss.push_back( hit.energyLoss() );
        thetaAtEntry.push_back( hit.thetaAtEntry() );
        phiAtEntry.push_back( hit.phiAtEntry() );
        tof.push_back( hit.tof() );
        particleType.push_back( hit.particleType() );
        detUnitId.push_back( detid );
        trackId.push_back( hit.trackId() );

        int pltNo,halfCarriageNo,telNo;
        int planeNo,rowNo,columnNo;

        std::tie(pltNo,halfCarriageNo,telNo,planeNo,rowNo,columnNo) = analyzeDetId(detid);
        int tempchannel = getChannel(pltNo,halfCarriageNo,telNo);
        int tempadc = getADC( hit.energyLoss() );

        channel.push_back(tempchannel);
        roc.push_back(planeNo);
        column.push_back(columnNo);
        row.push_back(rowNo);
        adc.push_back(tempadc);

    }

    tree->Fill();

    // clear the vectors for the next event
    pabs.clear();
    energyLoss.clear();
    thetaAtEntry.clear();
    phiAtEntry.clear();
    tof.clear();
    particleType.clear();
    detUnitId.clear();
    trackId.clear();
    channel.clear();
    roc.clear();
    column.clear();
    row.clear();
    adc.clear();

}


// ------------ method called once each job just before starting event loop  ------------
void 
PLTPileupProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PLTPileupProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
PLTPileupProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
PLTPileupProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
PLTPileupProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
PLTPileupProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PLTPileupProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PLTPileupProducer);
