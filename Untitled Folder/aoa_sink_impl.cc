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
#include "aoa_sink_impl.h"
 // Potrebno vkljuciti knjiznice ARMADILLO ter LAPACK
//#include <armadillo>

namespace gr {
  namespace customBlocks {

    aoa_sink::sptr
    aoa_sink::make(size_t vlen, const std::vector<float> array, float treshold, float fc)
    {
      return gnuradio::get_initial_sptr
        (new aoa_sink_impl(vlen, array, treshold, fc));
    }

    /*
     * The private constructor
     */
    aoa_sink_impl::aoa_sink_impl(size_t vlen, const std::vector<float> array, float treshold, float fc)
      : gr::sync_block("aoa_sink",
              gr::io_signature::make(1, -1, vlen * sizeof(gr_complex)),
              gr::io_signature::make(0, 0, 0)),
      d_vlen(vlen)
    {


    }

    /*
     * Our virtual destructor.
     */
    aoa_sink_impl::~aoa_sink_impl()
    {
    }

    int
    aoa_sink_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];

      // Do <+signal processing+>
      for(int i = 0; i < noutput_items; i++) {


      }
      //arma::mat AA = arma::randu<arma::mat>(5,5);
      //arma::vec HH = eig_sym(AA);

      //std::cout << HH << std::endl;
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace customBlocks */
} /* namespace gr */

