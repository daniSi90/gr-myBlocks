/* -*- c++ -*- */
/* 
 * Copyright 2014 Communications Engineering Lab, KIT.
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

#include "spectrogram_plot.h"
#include <iostream>
#include <stdexcept>

namespace gr {
	namespace myBlocks {

		spectrogram_plot::spectrogram_plot(int interval, std::vector<float> *buffer,
		QWidget* parent) : QWidget(parent)
		{
			std::string d_xlabel = "Angle";
			std::string d_ylabel = "Amplitude";
			d_interval = 2;
			d_buffer = buffer;
			
			// Setup GUI
			resize(QSize(600,600));
			
			d_plot = new QwtPlot(this); // make main plot
			// add curves
			curve = new QwtPlotCurve("Curve");
			curve->attach(d_plot);

			std::string label_title = "MuSIC Spectrum";
			d_plot->setTitle(QwtText(label_title.c_str())); 
			d_plot->setAxisTitle(QwtPlot::xBottom, d_xlabel.c_str());
			d_plot->setAxisTitle(QwtPlot::yLeft, d_ylabel.c_str());

			// Do replot
			d_plot->replot();

			// Setup timer and connect refreshing plot
			d_timer = new QTimer(this);
			connect(d_timer, SIGNAL(timeout()), this, SLOT(refresh()));
			d_timer->start(d_interval);

		}

		spectrogram_plot::~spectrogram_plot(){
		}
		
		void
		spectrogram_plot::resizeEvent( QResizeEvent * event ){
			d_plot->setGeometry(0,0,this->width(),this->height());
		}
		
		void
		spectrogram_plot::refresh(){
			

		    d_plot->setWindowTitle("QwtPlotCurve Line Width and Style");
			d_plot->setAxisScale(QwtPlot::xBottom,0,361);
			d_plot->setAxisScale(QwtPlot::yLeft,-7,3);

			QPolygonF data;
		    if((*d_buffer).size() > 0)
		    {
		        std::cout << (*d_buffer).size() << std::endl;
		        
		        for (int i = 0; i < (*d_buffer).size(); ++i)
		        {
		        	data << QPointF(i, (*d_buffer).at(i));
		        }
			    curve->setSamples(data);
				data.clear();  
			    
			    curve->setPen(* new QPen(Qt::blue,1,Qt::SolidLine));      
			    
			    curve->attach(d_plot);

			    d_plot->replot();
			    d_plot->show();
			   
			}
		}

	}
}
