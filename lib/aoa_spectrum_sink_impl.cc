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
#include "aoa_spectrum_sink_impl.h"

// Potrebno vkljuciti knjiznice ARMADILLO ter LAPACK
#include <armadillo>

#include <iostream>

using namespace arma;

namespace gr {
  namespace myBlocks {

    aoa_spectrum_sink::sptr
    aoa_spectrum_sink::make(size_t vlen, std::vector<float> array, float fc, float treshold)
    {
      return gnuradio::get_initial_sptr
        (new aoa_spectrum_sink_impl(vlen, array, fc, treshold));
    }

    /*
     * The private constructor
     */
    aoa_spectrum_sink_impl::aoa_spectrum_sink_impl(size_t vlen, std::vector<float> array, float fc, float treshold)
      : gr::sync_block("aoa_spectrum_sink",
              gr::io_signature::make(1, -1, vlen * sizeof(gr_complex)),
              gr::io_signature::make(0, 0, 0))
    {
      // Spremenljivke za MUSIC
      d_vlen = vlen;
      d_array = array;
      d_fc = fc;
      d_treshold = treshold;

      // Spremenljivke za plotanje
      d_interval = 0;
      d_xlabel = "Angle";
      d_ylabel = "Ratio";
      d_label = "";
      //d_axis_x = 0;
      //d_axis_y = 0;
      //d_axis_z = 0;
      d_autoscale_z = false;
      d_buffer.resize(0);
    
    // Setup GUI
    run_gui();
    }

    /*
     * Our virtual destructor.
     */
    aoa_spectrum_sink_impl::~aoa_spectrum_sink_impl()
    {
    }


    void
    aoa_spectrum_sink_impl::run_gui(){
      // Set QT window
      if(qApp != NULL) {
        d_qApplication = qApp;
      }
      else {
        d_argc = 1;
        d_argv = new char;
        d_argv[0] = '\0';
        d_qApplication = new QApplication(d_argc, &d_argv);
      }
      
      // Set QWT plot widget
      d_main_gui = new spectrogram_plot(d_interval, d_vlen, &d_buffer, d_xlabel, d_ylabel, d_label, d_axis_x, d_axis_y, d_axis_z, d_autoscale_z);
      d_main_gui->show();
    }

    int
    aoa_spectrum_sink_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      int noutput_items = 0;
      return noutput_items ;
    }

    int
    aoa_spectrum_sink_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {

      unsigned int n_items = input_items.size();
      // Input matrix
      cx_mat A(n_items,d_vlen);


      const gr_complex *in[n_items];
      for(size_t i = 0; i < n_items; i++)
      {
        in[i] = (const gr_complex *) input_items[i];

        for (int j = 0; j < d_vlen; ++j) A(i,j) = in[i][j];

      }
      //std::cout << "OK1" << std::endl;

      cx_mat rxx = (A * A.t());
      cx_vec eigval;
      cx_mat eigvec;
 
      //std::cout << "OK2" << std::endl;
      // Izracun lastnih vrednosti in lastnih vektorjev
      eig_gen(eigval, eigvec, rxx);      

   
      for (int i = 0; i < d_array.size(); ++i)
        if (real(eigval(i)) > d_treshold)
          eigvec.shed_cols(i,i);
      //std::cout << "OK3" << std::endl;
 
      vec az = linspace(0., 180., 361);
      vec el(az.size());
      //std::cout << "OK4" << std::endl;
      
      // SPV funkcija
      mat m_array(4,3);
      for (int i = 0; i < 4; ++i)
        m_array(i,0) = d_array.at(i);

      vec az_rad = az * M_PI / 180;
      mat ki(3,361);
      ki.row(0) = 2.f * d_fc / 3e8 * M_PI * (cos(az_rad.t()) % cos(el.t()));
      ki.row(1) = 2.f * d_fc / 3e8 * M_PI * (sin(az_rad.t()) % cos(el.t()));
      ki.row(2) = 2.f * d_fc / 3e8 * M_PI * sin(el.t());
      cx_mat S(cos(m_array * ki), -sin(m_array * ki));

      //std::cout << "OK5" << std::endl;
      vec Z(1);
      vec Z_f(361);
      cx_mat S_t = S.t();
      /* ********************** CALC SPECTRUM ********************** */
      d_buffer.clear();
      for (int i = 0; i < 361; ++i)
      {
        Z = abs(S_t.row(i) * eigvec * eigvec.t() * S.col(i));
        Z_f(i) = -10 * log10(Z(0));
        d_buffer.push_back(Z_f(i));
      }

      //for(int i=0; i<d_buffer.size(); ++i)
      //std::cout << d_buffer.at(i) << ' ';
      //std::cout << "OK6" << std::endl;
      //Z_f.print("Angle:");
      
      // Copy data to shared buffer with GUI

      //memcpy(&d_buffer[0], in[0], sizeof(float)*d_vlen);
      

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace myBlocks */
} /* namespace gr */

