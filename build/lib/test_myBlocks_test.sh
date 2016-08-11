#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/ubuntu/projects/gr-myBlocks/lib
export PATH=/home/ubuntu/projects/gr-myBlocks/build/lib:$PATH
export LD_LIBRARY_PATH=/home/ubuntu/projects/gr-myBlocks/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-myBlocks 
