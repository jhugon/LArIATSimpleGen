import ROOT
from ROOT import *
from math import pi, sin, cos
import sys,os
import argparse


# This code takes as an argument the file 
# we need to generate metadata for
parser = argparse.ArgumentParser()
parser.add_argument("fname"   , nargs='?', default = '../MomentumManipulation/anaTree_postTOFReco.root', type = str, help="insert fileName")
parser.add_argument("treeName", nargs='?', default = 'anatree/anatree'          , type = str, help="insert treeName")

args = parser.parse_args()
fname     = args.fname   
treeName  = args.treeName


f = ROOT.TFile(fname)
t = f.Get(treeName)
#t.Print()


hwcPTot = TH1F("hwcPTot","hwcPTot",200,0,2000)
hwcPxTot= TH1F("hwcPxTot","hwcPzTot",200,-200,0)
hwcPyTot= TH1F("hwcPyTot","hwcPyTot",200,-100,100)
hwcPzTot= TH1F("hwcPzTot","hwcPzTot",200,0,2000)
hwcThetaTot= TH1F("hwcThetaTot","hwcThetaTot",200,0,0.2)
hwcPhiTot  = TH1F("hwcPhiTot","hwcPhiTot",800,-4.,4.)
hwcPhiTotNotFUp  = TH1F("hwcPhiTotNotFUp","hwcPhiTotNotFUp",6400,0.,6.4)
hwcPhiTotNotFUpDecentBinning  = TH1F("hwcPhiTotNotFUpDecentBinning","hwcPhiTotNotFUpDecentBinning",200,2.,4.)

hwcPhiVsTheta  = TH2F("hwcPhiVsTheta","hwcPhiVsTheta",200,0,0.2,200,2.,4.)

hwcThetaVsP  = TH2F("hwcThetaVsP","hwcThetaVsP"   ,200,0,0.2,200,0,2000)
hwcPhiVsP    = TH2F("hwcPhiVsP","hwcPhiVsP",200,2.,4.,200,0,2000)
hwcPhiVsThetaVsP  = TH3F("hwcPhiVsThetaVsP","hwcPhiVsThetaVsP",200,0,0.2,200,2.,4.,200,0,2000)

hWC4XvsY    = TH2F("hWC4XvsY","hWC4XvsY"  , 200 , 20., 40., 140, -7., 7.)
hPvsWC4Y    = TH2F("hPvsWC4Y","hPvsWC4Y"  , 140 , -7.,  7., 200,  0., 2000)
hPvsWC4X    = TH2F("hPvsWC4X","hPvsWC4X"  , 200 , 20., 40., 200,  0., 2000)
hwcXVsYVsP  = TH3F("hwcXVsYVsP","hwcXVsYVsP", 200 , 20., 40., 140, -7., 7., 200 , 0. , 2000.)


hWC4X    = TH1F("hWC4X","hWC4X"  , 200 , 20., 40.)
hWC4Y    = TH1F("hWC4Y","hWC4Y"  , 140 , -7.,  7.)

print "{} Events Total".format(t.GetEntries())
print "I'm looping on your tree, this might take some minutes"
stupidCounter = 0 
for event in t:
    stupidCounter += 1
    #if stupidCounter > 1000: break
    if not stupidCounter % 10000.:
        print "Event: ", stupidCounter 
    if event.nwctrks < 1:
        continue
    wcP = event.wctrk_momentum[0]
    if wcP > 10:
        theta  = event.wctrk_theta[0]
        phi  = event.wctrk_phi[0]
        wcPx = wcP*sin(theta)*cos(phi)
        wcPy = wcP*sin(theta)*sin(phi)
        wcPz = wcP*cos(theta)
        hwcPTot.Fill(wcP)
        hwcPxTot.Fill(wcPx)
        hwcPyTot.Fill(wcPy)
        hwcPzTot.Fill(wcPz)
        hwcThetaTot.Fill(theta)
        hwcPhiTot  .Fill(phi)

        WC4x = float(event.WC4xPos[0])#/10.
        WC4y = float(event.WC4yPos[0])#/10.

        hWC4XvsY.Fill(WC4x,WC4y)
        hPvsWC4Y.Fill(WC4y,wcP)
        hPvsWC4X.Fill(WC4x,wcP)
        hwcXVsYVsP.Fill(WC4x,WC4y,wcP)
        hWC4X.Fill(WC4x)
        hWC4Y.Fill(WC4y)

        if phi<0:
          phi += 2*pi

        hwcPhiTotNotFUp.Fill(phi) 
        hwcPhiTotNotFUpDecentBinning.Fill(phi) 
        hwcPhiVsTheta.Fill(theta,phi)
        hwcPhiVsP.Fill(phi,wcP)
        hwcThetaVsP.Fill(theta,wcP)
        hwcPhiVsThetaVsP.Fill(theta,phi,wcP)

outFile = TFile("simpleGen.root","RECREATE")
outFile.Add(hwcPTot)
outFile.Add(hwcPxTot)
outFile.Add(hwcPyTot)
outFile.Add(hwcPzTot)
outFile.Add(hwcThetaTot)
outFile.Add(hwcPhiTot)
outFile.Add(hwcPhiTotNotFUp)
outFile.Add(hwcPhiTotNotFUpDecentBinning)
outFile.Add(hwcPhiVsTheta)
outFile.Add(hwcPhiVsThetaVsP)
outFile.Add(hwcPhiVsP)
outFile.Add(hwcThetaVsP)
outFile.Add(hWC4XvsY)  
outFile.Add(hPvsWC4Y) 
outFile.Add(hPvsWC4X)
outFile.Add(hwcXVsYVsP)

outFile.Add(hWC4X)
outFile.Add(hWC4Y)
outFile.Write()




    
