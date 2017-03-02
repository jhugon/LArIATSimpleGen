#!/bin/bash

makehepandsplit () {
    if [ -z "$1" ]                           # Is parameter #1 zero length?
    then
      echo "Error: makehepandsplit needs a pdg code as first argument"  # Or no parameter passed.
      return 1
    else
      echo "Making pdg=$1"
    fi
    if [ -z "$2" ]                           # Is parameter #2 zero length?
    then
      echo "Error: makehepandsplit needs a number of events to split as second argument"  # Or no parameter passed.
      return 1
    else
      echo "Nevents per chunk=$2"
    fi
 
    neventstimes2=$(( $2 * 2 ))
    infilename=LArIATHepEvt_pdg_"$1".txt
    outdir=$basedir/$1
    outprefix=$outdir/LArIATHepEvt_pdg_"$1"_chunk"$2"_
    echo "Output directory: $outdir"
    python generateHEPEvt.py $1 GeneratedEvents.root
    mkdir -p $outdir
    split -l $neventstimes2 -d -a 5 $infilename $outprefix 
}

##########################################################################

basedir=/pnfs/lariat/scratch/users/jhugon/v06_15_00/HEPEvt_Pos_RunI_v03_v2
#mkdir -p $basedir

pdg=321
nevents=700
makehepandsplit $pdg $nevents

pdg=-13
nevents=550
makehepandsplit $pdg $nevents

pdg=211
nevents=750
makehepandsplit $pdg $nevents

pdg=-11
nevents=300
makehepandsplit $pdg $nevents

pdg=2212
nevents=1100
makehepandsplit $pdg $nevents
