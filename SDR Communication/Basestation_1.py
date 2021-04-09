#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Basestation 1
# GNU Radio version: 3.7.13.5
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import pmt
import sys
import time
import os
import shutil
from gnuradio import qtgui


class Basestation_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Basestation 1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Basestation 1")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "Basestation_1")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 800000
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(('serial=30AD2B6', 'serial=30AD2B6')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_center_freq(2500000000, 0)
        self.uhd_usrp_sink_0.set_gain(70, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_center_freq(2500000000, 1)
        self.uhd_usrp_sink_0.set_gain(70, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/capstone2021/Desktop/Capstone/fire_scout_system/ground_station/drone_ops.json', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=True,
        	),
        	payload_length=4,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.uhd_usrp_sink_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Basestation_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1


class Basestation_3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Basestation 3")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Basestation 3")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "Basestation_3")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 800000
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source = uhd.usrp_source(
        	",".join(('serial=30AD2B6', 'serial=30AD2B6')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		args='peak=0.003906',
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source.set_samp_rate(samp_rate)
        self.uhd_usrp_source.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source.set_center_freq(2400000000, 0)
        self.uhd_usrp_source.set_gain(50, 0)
        self.uhd_usrp_source.set_antenna('RX2', 0)
        self.uhd_usrp_source.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source.set_center_freq(2400000000, 1)
        self.uhd_usrp_source.set_gain(50, 1)
        self.uhd_usrp_source.set_antenna('RX2', 1)
        self.uhd_usrp_source.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source.set_auto_iq_balance(True, 1)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 200000, 50000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, samp_rate/4, samp_rate/8, firdes.WIN_HAMMING, 6.76))
        self.digital_gmsk_demod_0_0 = digital.gmsk_demod(
        	samples_per_symbol=2,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=2,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_char*1, '/home/capstone2021/Desktop/Gun software/file_receive/Text/Text_recie.txt', append=False)
        self.blocks_file_sink_1.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/capstone2021/Desktop/Gun software/file_receive/Jpg/Jpg_receive.jpg', append=False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_packet_decoder_0_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0.recv_pkt(ok, payload),
        	),
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_packet_decoder_0_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_gmsk_demod_0_0, 0), (self.blks2_packet_decoder_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_gmsk_demod_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.digital_gmsk_demod_0_0, 0))
        self.connect((self.uhd_usrp_source, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.uhd_usrp_source, 1), (self.low_pass_filter_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Basestation_3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 200000, 50000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/4, self.samp_rate/8, firdes.WIN_HAMMING, 6.76))

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1

def main(top_block_cls_1=Basestation_3,top_block_cls_2=Basestation_1,options=None):
    open('/home/capstone2021/Desktop/Capstone/fire_scout_system/ground_station/drone_ops.json','a').close()
    open('/home/capstone2021/Desktop/Gun software/file_receive/Text/Text_recie.txt','a').close()
    open('/home/capstone2021/Desktop/Gun software/file_receive/Jpg/Jpg_receive.jpg','a').close()
    qapp = Qt.QApplication(sys.argv)
    tb1 = top_block_cls_1()
    tb1.start()
    Jpg_count_number = 1
    Txt_count_number = 1
    filesize = 0
    filesize_1 = 0
    filesize_2 = 0
    while 1:
     	Deter_mode = os.path.getsize('/home/capstone2021/Desktop/Gun software/Mod_com.txt')
     	filesize = os.path.getsize('/home/capstone2021/Desktop/Capstone/fire_scout_system/ground_station/drone_ops.json')
	if filesize != 0:
		tb2 = top_block_cls_2()
	     	tb2.start()
            	time.sleep(2)
     	    	tb2.stop()

	    	os.remove('/home/capstone2021/Desktop/Capstone/fire_scout_system/ground_station/drone_ops.json')
	     	open('/home/capstone2021/Desktop/Capstone/fire_scout_system/ground_station/drone_ops.json','a').close()
		print('commond sent')
	filesize_1 = os.path.getsize('/home/capstone2021/Desktop/Gun software/file_receive/Text/Text_recie.txt')
	if filesize_1 != 0:
		if Deter_mode == 0:
			if Txt_count_number > 1 :
				os.remove('/home/capstone2021/Desktop/Gun software/Watch_dog.txt')
			open('/home/capstone2021/Desktop/Gun software/Watch_dog.txt','a').close()
			textFile = '/home/capstone2021/Desktop/Gun software/file_receive/Text/TxT_Receiver_%d.txt' % Txt_count_number
			shutil.move('/home/capstone2021/Desktop/Gun software/file_receive/Text/Text_recie.txt', textFile)
			time.sleep(1)
			with open('/home/capstone2021/Desktop/Gun software/file_receive/Text/TxT_Receiver_%d.txt' % Txt_count_number) as firstfile, open('/home/capstone2021/Desktop/Gun software/Watch_dog.txt','w') as secondfile:
				for line in firstfile:
					secondfile.write(line)
				secondfile.close()
			Txt_count_number += 1
			open('/home/capstone2021/Desktop/Gun software/file_receive/Text/Text_recie.txt','a').close()
			print ('get txt')
			tb1.stop()
			tb1 = top_block_cls_1()
			tb1.start()
		else :
			textFile = '/home/capstone2021/Desktop/Capstone/fire_scout_system/ground_station/received_data/new_image_%d.jpg' % Jpg_count_number
			
			Jpg_count_number += 1
			open('/home/capstone2021/Desktop/Gun software/file_receive/Text/Text_recie.txt','a').close()
			print ('get jpg')
			time.sleep(10)
			tb1.stop()
			shutil.move('/home/capstone2021/Desktop/Gun software/file_receive/Text/Text_recie.txt', textFile)
			
			tb1 = top_block_cls_1()
			tb1.start()
    tb1.stop()




if __name__ == '__main__':
    main()
