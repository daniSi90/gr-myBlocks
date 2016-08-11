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

#include <complex>

#include <QApplication>
#include <QTimer>
#include <QWidget>

#include <qwt_plot.h>
#include <qwt_plot_curve.h>
#include <qwt_color_map.h>
#include <qwt_plot_spectrogram.h>
#include <qwt_matrix_raster_data.h>
#include <qwt_scale_widget.h>

namespace gr {
	namespace myBlocks {
		
		class spectrogram_plot : public QWidget
		{
		Q_OBJECT

		public:
			spectrogram_plot(int interval, std::vector<float> *buffer,
			QWidget* parent = 0);
			~spectrogram_plot();
			
		private:
			int d_interval;
			std::vector<float> *d_buffer;
			QTimer *d_timer;
			
			QwtPlot *d_plot;
			QwtPlotSpectrogram *d_spectrogram;
			QwtMatrixRasterData *d_data;
			QwtLinearColorMap *d_colormap;
			QwtScaleWidget *d_scale;
			
			QVector<double> d_plot_data;

			QwtPlotCurve *curve;
			
			
		protected:
			void resizeEvent(QResizeEvent * event);
			
		public slots:
			void refresh();
			
		};


		class CosinusData: public QwtSyntheticPointData
		{
		public:
	    	CosinusData(size_t numberOfPoints):
        	QwtSyntheticPointData(numberOfPoints)
		    {
		    }
    
	    	//This has to be overridden, because it is pure virtual in base class
		    double y(double x) const
		    {
		        return 500*qCos(x);
		    }
		};


	}
}
