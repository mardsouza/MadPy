#!/bin/bash

# Activate python2
module load python2.7

export MADGRAPH2='../mg5amcnlo-2.9.24'
export SCRIPT_PATH='../notebooks/maddm_script.txt'

python2.7 $MADGRAPH2/bin/maddm.py $SCRIPT_PATH