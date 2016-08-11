#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Usrp Angle Of Arrival
# Generated: Thu Aug 11 11:40:29 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import myBlocks
import sys
import time


class usrp_angle_of_arrival(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Usrp Angle Of Arrival")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Usrp Angle Of Arrival")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "usrp_angle_of_arrival")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.vec_size = vec_size = 1024
        self.usrp2_gain = usrp2_gain = 40
        self.usrp1_gain = usrp1_gain = 40
        self.tresh = tresh = 100
        self.transition_h = transition_h = 10e3
        self.transition = transition = 10e3
        self.tar_gain = tar_gain = 40
        self.tar_freq_0 = tar_freq_0 = 100e3
        self.tar_freq = tar_freq = 100e3
        self.samp_rate = samp_rate = 1e6
        self.ref_gain = ref_gain = 16
        self.ref_freq = ref_freq = 10e3
        self.keep = keep = 250
        self.gain_h = gain_h = 2
        self.gain = gain = 2
        self.cut_off_h = cut_off_h = 90e3
        self.cut_off = cut_off = 15e3
        self.center_freq = center_freq = 1.3e9

        ##################################################
        # Blocks
        ##################################################
        self._usrp2_gain_range = Range(0, 100, 1, 40, 200)
        self._usrp2_gain_win = RangeWidget(self._usrp2_gain_range, self.set_usrp2_gain, "usrp2_gain", "counter_slider", float)
        self.top_layout.addWidget(self._usrp2_gain_win)
        self._usrp1_gain_range = Range(0, 100, 1, 40, 200)
        self._usrp1_gain_win = RangeWidget(self._usrp1_gain_range, self.set_usrp1_gain, "usrp1_gain", "counter_slider", float)
        self.top_layout.addWidget(self._usrp1_gain_win)
        self._tresh_range = Range(0.01, 5000, 0.01, 100, 200)
        self._tresh_win = RangeWidget(self._tresh_range, self.set_tresh, "tresh", "counter_slider", float)
        self.top_layout.addWidget(self._tresh_win)
        self._tar_gain_range = Range(0, 100, 1, 40, 200)
        self._tar_gain_win = RangeWidget(self._tar_gain_range, self.set_tar_gain, "tar_gain", "counter_slider", float)
        self.top_layout.addWidget(self._tar_gain_win)
        self._ref_gain_range = Range(0, 100, 1, 16, 200)
        self._ref_gain_win = RangeWidget(self._ref_gain_range, self.set_ref_gain, "ref_gain", "counter_slider", float)
        self.top_layout.addWidget(self._ref_gain_win)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("addr=164.8.30.121", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0_0.set_clock_source("external", 0)
        self.uhd_usrp_source_0_0.set_time_source("external", 0)
        self.uhd_usrp_source_0_0.set_subdev_spec("A:0 B:0", 0)
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0_0.set_gain(usrp2_gain, 0)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0_0.set_gain(usrp2_gain, 1)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.40.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source("external", 0)
        self.uhd_usrp_source_0.set_time_source("external", 0)
        self.uhd_usrp_source_0.set_subdev_spec("A:0 B:0", 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(usrp1_gain, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0.set_gain(usrp1_gain, 1)
        self.uhd_usrp_source_0.set_antenna("RX2", 1)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("addr=164.8.30.119", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0_0.set_gain(tar_gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=164.8.30.120", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0.set_gain(ref_gain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.myBlocks_phaseSync_cc_0 = myBlocks.phaseSync_cc()
        self.myBlocks_aoa_spectrum_sink_0 = myBlocks.aoa_spectrum_sink(vec_size, (0, 0.1154, 0.2308, 0.3462), center_freq, tresh)
        self.low_pass_filter_0_2 = filter.fir_filter_ccf(1, firdes.low_pass(
        	gain, samp_rate, cut_off, transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	gain, samp_rate, cut_off, transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	gain, samp_rate, cut_off, transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	gain, samp_rate, cut_off, transition, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_2 = filter.fir_filter_ccf(1, firdes.high_pass(
        	gain_h, samp_rate, cut_off_h, transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_1 = filter.fir_filter_ccf(1, firdes.high_pass(
        	gain_h, samp_rate, cut_off_h, transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.high_pass(
        	gain_h, samp_rate, cut_off_h, transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_ccf(1, firdes.high_pass(
        	gain_h, samp_rate, cut_off_h, transition_h, firdes.WIN_HAMMING, 6.76))
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_size)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_size)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_size)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_size)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_keep_one_in_n_0_2 = blocks.keep_one_in_n(gr.sizeof_gr_complex*vec_size, keep)
        self.blocks_keep_one_in_n_0_1 = blocks.keep_one_in_n(gr.sizeof_gr_complex*vec_size, keep)
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*vec_size, keep)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*vec_size, keep)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, tar_freq, 0.5, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, ref_freq, 0.5, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.uhd_usrp_sink_0_0, 0))    
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.myBlocks_aoa_spectrum_sink_0, 0))    
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.myBlocks_aoa_spectrum_sink_0, 1))    
        self.connect((self.blocks_keep_one_in_n_0_1, 0), (self.myBlocks_aoa_spectrum_sink_0, 2))    
        self.connect((self.blocks_keep_one_in_n_0_2, 0), (self.myBlocks_aoa_spectrum_sink_0, 3))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_stream_to_vector_0_1, 0))    
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_keep_one_in_n_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_keep_one_in_n_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.blocks_keep_one_in_n_0_2, 0))    
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_keep_one_in_n_0_1, 0))    
        self.connect((self.high_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.high_pass_filter_0_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.high_pass_filter_0_1, 0), (self.blocks_multiply_xx_0_1, 0))    
        self.connect((self.high_pass_filter_0_2, 0), (self.blocks_multiply_xx_0_2, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.myBlocks_phaseSync_cc_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.myBlocks_phaseSync_cc_0, 1))    
        self.connect((self.low_pass_filter_0_1, 0), (self.myBlocks_phaseSync_cc_0, 2))    
        self.connect((self.low_pass_filter_0_2, 0), (self.myBlocks_phaseSync_cc_0, 3))    
        self.connect((self.myBlocks_phaseSync_cc_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.myBlocks_phaseSync_cc_0, 1), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.myBlocks_phaseSync_cc_0, 2), (self.blocks_multiply_xx_0_1, 1))    
        self.connect((self.myBlocks_phaseSync_cc_0, 3), (self.blocks_multiply_xx_0_2, 1))    
        self.connect((self.uhd_usrp_source_0, 0), (self.high_pass_filter_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.high_pass_filter_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.low_pass_filter_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.high_pass_filter_0_1, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.high_pass_filter_0_2, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.low_pass_filter_0_1, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.low_pass_filter_0_2, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "usrp_angle_of_arrival")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vec_size(self):
        return self.vec_size

    def set_vec_size(self, vec_size):
        self.vec_size = vec_size

    def get_usrp2_gain(self):
        return self.usrp2_gain

    def set_usrp2_gain(self, usrp2_gain):
        self.usrp2_gain = usrp2_gain
        self.uhd_usrp_source_0_0.set_gain(self.usrp2_gain, 0)
        	
        self.uhd_usrp_source_0_0.set_gain(self.usrp2_gain, 1)
        	

    def get_usrp1_gain(self):
        return self.usrp1_gain

    def set_usrp1_gain(self, usrp1_gain):
        self.usrp1_gain = usrp1_gain
        self.uhd_usrp_source_0.set_gain(self.usrp1_gain, 0)
        	
        self.uhd_usrp_source_0.set_gain(self.usrp1_gain, 1)
        	

    def get_tresh(self):
        return self.tresh

    def set_tresh(self, tresh):
        self.tresh = tresh

    def get_transition_h(self):
        return self.transition_h

    def set_transition_h(self, transition_h):
        self.transition_h = transition_h
        self.high_pass_filter_0_2.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_1.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_tar_gain(self):
        return self.tar_gain

    def set_tar_gain(self, tar_gain):
        self.tar_gain = tar_gain
        self.uhd_usrp_sink_0_0.set_gain(self.tar_gain, 0)
        	

    def get_tar_freq_0(self):
        return self.tar_freq_0

    def set_tar_freq_0(self, tar_freq_0):
        self.tar_freq_0 = tar_freq_0

    def get_tar_freq(self):
        return self.tar_freq

    def set_tar_freq(self, tar_freq):
        self.tar_freq = tar_freq
        self.analog_sig_source_x_0_0.set_frequency(self.tar_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_2.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_1.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_ref_gain(self):
        return self.ref_gain

    def set_ref_gain(self, ref_gain):
        self.ref_gain = ref_gain
        self.uhd_usrp_sink_0.set_gain(self.ref_gain, 0)
        	

    def get_ref_freq(self):
        return self.ref_freq

    def set_ref_freq(self, ref_freq):
        self.ref_freq = ref_freq
        self.analog_sig_source_x_0.set_frequency(self.ref_freq)

    def get_keep(self):
        return self.keep

    def set_keep(self, keep):
        self.keep = keep
        self.blocks_keep_one_in_n_0_2.set_n(self.keep)
        self.blocks_keep_one_in_n_0_1.set_n(self.keep)
        self.blocks_keep_one_in_n_0_0.set_n(self.keep)
        self.blocks_keep_one_in_n_0.set_n(self.keep)

    def get_gain_h(self):
        return self.gain_h

    def set_gain_h(self, gain_h):
        self.gain_h = gain_h
        self.high_pass_filter_0_2.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_1.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_cut_off_h(self):
        return self.cut_off_h

    def set_cut_off_h(self, cut_off_h):
        self.cut_off_h = cut_off_h
        self.high_pass_filter_0_2.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_1.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(self.gain_h, self.samp_rate, self.cut_off_h, self.transition_h, firdes.WIN_HAMMING, 6.76))

    def get_cut_off(self):
        return self.cut_off

    def set_cut_off(self, cut_off):
        self.cut_off = cut_off
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.cut_off, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_sink_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=usrp_angle_of_arrival, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
