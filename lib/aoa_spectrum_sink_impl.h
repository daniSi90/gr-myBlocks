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

#ifndef INCLUDED_MYBLOCKS_AOA_SPECTRUM_SINK_IMPL_H
#define INCLUDED_MYBLOCKS_AOA_SPECTRUM_SINK_IMPL_H

#include <myBlocks/aoa_spectrum_sink.h>

#include "spectrogram_plot.h"
 
namespace gr {
  namespace myBlocks {

    class aoa_spectrum_sink_impl : public aoa_spectrum_sink
    {
     private:
      // Nothing to declare in this block.
     
     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      aoa_spectrum_sink_impl(size_t vlen, std::vector<float> array, float fc, float treshold);
      ~aoa_spectrum_sink_impl();
      
      size_t d_vlen;
      std::vector<float> d_array;
      float d_fc;
      float d_treshold;

      // RUN GUI
      void run_gui();
      
      int d_argc;
      char *d_argv;
      QApplication *d_qApplication;
      
      int d_interval;
      std::string d_xlabel, d_ylabel, d_label;
      std::vector<float> d_axis_x, d_axis_y, d_axis_z;
      std::vector<float> d_buffer;
      
      bool d_autoscale_z;
      spectrogram_plot* d_main_gui;
      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace myBlocks
} // namespace gr

#endif /* INCLUDED_MYBLOCKS_AOA_SPECTRUM_SINK_IMPL_H */

