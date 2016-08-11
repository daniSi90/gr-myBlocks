/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "phaseSync_cc_impl.h"
#include <gnuradio/math.h>
#include <volk/volk.h>

#include <iostream>

namespace gr {
  namespace myBlocks {

    phaseSync_cc::sptr
    phaseSync_cc::make()
    {
      return gnuradio::get_initial_sptr
        (new phaseSync_cc_impl());
    }

    /*
     * The private constructor
     */
    phaseSync_cc_impl::phaseSync_cc_impl()
      : gr::sync_block("phaseSync_cc",
              gr::io_signature::make(1, -1, sizeof(gr_complex)),
              gr::io_signature::make(1, -1, sizeof(gr_complex)))
    {}

    /*
     * Our virtual destructor.
     */
    phaseSync_cc_impl::~phaseSync_cc_impl()
    {
    }

    int
    phaseSync_cc_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      // Preveri koliko vhodov/izhodov je in ustrezno nastavi parametre
      unsigned int i_sz = input_items.size();
      unsigned int o_sz = output_items.size();
      if(i_sz != o_sz){
          std::cout << "PhaseSync Input/Output dimension mismatch!" << std::endl;
          return -1;
      }
      else{
          const gr_complex *in[i_sz];
          gr_complex *out[o_sz];

          for (int i = 0; i < i_sz; ++i)
          {
            in[i] = (const gr_complex *) input_items[i];
            out[i] = (gr_complex *) output_items[i];
          }

          gr_complex xc;  // rabi se n-1 elementov
          float ph_xc;


          // PHASE SYNC
          for (int i = 0; i < i_sz; ++i) // gre od 1 naprej ker je "0" element referenca
          {
            for (int j = 0; j < noutput_items; j++){
              xc = in[0][j] / in[i][j];
              ph_xc = gr::fast_atan2f(xc);
              out[i][j] = gr_complex (cos(ph_xc), sin(ph_xc));
            }
          }
      
      }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace myBlocks */
} /* namespace gr */

