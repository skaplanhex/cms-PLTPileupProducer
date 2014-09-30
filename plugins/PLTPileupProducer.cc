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
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      edm::Service<TFileService> fs;
      TTree* tree;
      static const int maxNHits = 500;
      int nHits;
      int eventNum;
      bool hasHits;
      float pabs[maxNHits];
      float energyLoss[maxNHits];
      float thetaAtEntry[maxNHits];
      float phiAtEntry[maxNHits];
      float tof[maxNHits];
      int particleType[maxNHits];
      int detUnitId[maxNHits];
      int trackId[maxNHits];


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

    tree = fs->make<TTree>("tree","tree");
    tree->Branch("eventNum",&eventNum,"eventNum/I");
    tree->Branch("hasHits",&hasHits,"hasHits/O");
    tree->Branch("nHits",&nHits,"nHits/I");
    tree->Branch("pabs",pabs,"pabs[nHits]/F");
    tree->Branch("energyLoss",energyLoss,"energyLoss[nHits]/F");
    tree->Branch("thetaAtEntry",thetaAtEntry,"thetaAtEntry[nHits]/F");
    tree->Branch("phiAtEntry",phiAtEntry,"phiAtEntry[nHits]/F");
    tree->Branch("tof",tof,"tof[nHits]/F");
    tree->Branch("particleType",particleType,"particleType[nHits]/I");
    tree->Branch("detUnitId",detUnitId,"detUnitId[nHits]/I");
    tree->Branch("trackId",trackId,"trackId[nHits]/I");

}


PLTPileupProducer::~PLTPileupProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
PLTPileupProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    eventNum = (int)iEvent.id().event();

    edm::Handle<PSimHitContainer> simHitHandle;
    edm::InputTag tag("g4SimHits","PLTHits","SIM");
    iEvent.getByLabel(tag,simHitHandle);
    nHits = simHitHandle->size();
    hasHits = (nHits>0 ? true : false);

    for (int iHit = 0; iHit < (int)simHitHandle->size(); iHit++){
        PSimHit hit = simHitHandle->at(iHit);
        pabs[iHit] = hit.pabs();
        energyLoss[iHit] = hit.energyLoss();
        thetaAtEntry[iHit] = hit.thetaAtEntry();
        phiAtEntry[iHit] = hit.phiAtEntry();
        tof[iHit] = hit.tof();
        particleType[iHit] = hit.particleType();
        detUnitId[iHit] = hit.detUnitId();
        trackId[iHit] = hit.trackId();
    }

    tree->Fill();

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
