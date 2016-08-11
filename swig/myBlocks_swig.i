/* -*- c++ -*- */

#define MYBLOCKS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "myBlocks_swig_doc.i"

%{
#include "myBlocks/phaseSync_cc.h"
#include "myBlocks/aoa_spectrum_sink.h"
%}


%include "myBlocks/phaseSync_cc.h"
GR_SWIG_BLOCK_MAGIC2(myBlocks, phaseSync_cc);

%include "myBlocks/aoa_spectrum_sink.h"
GR_SWIG_BLOCK_MAGIC2(myBlocks, aoa_spectrum_sink);
