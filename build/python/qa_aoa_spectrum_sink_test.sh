#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/ubuntu/projects/gr-myBlocks/python
export PATH=/home/ubuntu/projects/gr-myBlocks/build/python:$PATH
export LD_LIBRARY_PATH=/home/ubuntu/projects/gr-myBlocks/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/ubuntu/projects/gr-myBlocks/build/swig:$PYTHONPATH
/usr/bin/python2 /home/ubuntu/projects/gr-myBlocks/python/qa_aoa_spectrum_sink.py 
