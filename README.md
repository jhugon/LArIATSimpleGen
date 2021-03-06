# LArIATSimpleGen
Description of this Package:
This is a simple MC generator for single particle gun in LArIAT. 
The general idea is to exploit our knowledge of the Wire Chamber data in order to 
construct a realistic single particle MC.


What does this package contain?

<ol>
  <li>README.md</li>
  <li>plotDataDistributions.py</li>      
  <li>XYMomentumGenTTree.py  </li>
  <li>generateHEPEvt.py      </li>
  <li>myLittleGenerator3DTTree.py </li>
  <li>prodText.fcl</li>
  <li>referenceTree.root</li>	    
</ol>


<b> So, I want to generate some single particle MC... what do I need?</b>

<ol>
<li> To download this package. And you can do so by 
 > git clone  https://github.com/ElenaGramellini/LArIATSimpleGen
</li>
<li> The LArIAT anatree file for the DATA  you want to mimick the behavior of.
 e.g. you want to mimick RUN II proton at p = 200 MeV/c? Select them in DATA and feed your anatree to this package
</li>
<li> We want to start from the data distributions. So, Launch plotDataDistributions.py on your anatree. Like this:
<br/><br />
> plotDataDistributions.py <fileName> <TTreeName>
<br/><br />
This step will produce a root file called "simpleGen.root"
</li>
<li> Launch the generator. You can simulate the Momentum Profile alone or the Momentum Profile and the X Y position on WC4
<br />  <br />
  4.1 If you want to generate the Momentum Profile alone
<br /><br />
      > myLittleGenerator3DTTree.py
<br /><br />
  4.2 If you want to take into account the XY position do the following:
<br /><br />
      > XYMomentumGenTTree.py
<br /><br />
in the same folder where simpleGen.root is.
This step is going to take quite a while... To generate ~360000 events with correct XY and P, you need to throw about 200000000 tries and it take ~4 hrs. This setp will produce a root file called "GeneratedEvents.root". This file contains a TTree with the generated events. The variables stored in the TTree are: momentumTot, momentumX, momentumY, momentumZ, theta, phi, WC4X, WC4Y      </li>

<li> Transform the TTree to a HEPEvt format (so it can be read by a LArSoft module)
<br /><br />
> generateHEPEvt.py <pdg> <fileName> <TTreeName>
<br /><br />
Note: <fileName> <TTreeName> are optional. If you leave them blank and you haven't messed around with names in the previous steps, it should work.
You NEED the pdg code of your particle though.
This step will generate a text file with HEP format events.
</li>

<li>
 Take your text file with HEP format events and feed it into the LArSoft module TextFileGen. I use prodText.fcl (in the package for reference), but you're on your own on this one...
</li>
</ol>