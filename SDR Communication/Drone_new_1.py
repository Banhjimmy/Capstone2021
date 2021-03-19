#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Test
# Generated: Wed Mar  3 16:18:43 2021
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx
import os
import pmt
import shutil


class Drone_1(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Test")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 800000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(('serial=319B8D3', 'serial=319B8D3')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_center_freq(2500000000, 0)
        self.uhd_usrp_source_1.set_gain(50, 0)
        self.uhd_usrp_source_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 200000, 50000, firdes.WIN_HAMMING, 6.76))
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=2,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_rec.txt', False)
        self.blocks_file_sink_0.set_unbuffered(True)
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
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_gmsk_demod_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.low_pass_filter_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 200000, 50000, firdes.WIN_HAMMING, 6.76))

class Drone_2(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Test")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 800000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink = uhd.usrp_sink(
        	",".join(('serial=319B8D3', 'serial=319B8D3')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink.set_samp_rate(samp_rate)
        self.uhd_usrp_sink.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink.set_center_freq(2400000000, 0)
        self.uhd_usrp_sink.set_gain(70, 0)
        self.uhd_usrp_sink.set_antenna('TX/RX', 0)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_sent.txt', False)
        self.blks2_packet_encoder_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
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
        self.connect((self.blks2_packet_encoder_0_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.uhd_usrp_sink, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

class Drone_4(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Drone 4")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 800000
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink = uhd.usrp_sink(
        	",".join(('serial=319B8D3', 'serial=319B8D3')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink.set_samp_rate(samp_rate)
        self.uhd_usrp_sink.set_center_freq(2400000000, 0)
        self.uhd_usrp_sink.set_gain(80, 0)
        self.uhd_usrp_sink.set_antenna('TX/RX', 0)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate*2,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Jpg_sent.jpg', False)
        self.blks2_packet_encoder_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=True,
        	),
        	payload_length=0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_encoder_0_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*2)

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1



def main(top_block_cls_1=Drone_1 , top_block_cls_2=Drone_2 , top_block_cls_4=Drone_4 , options=None):
    open('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_rec.txt','a').close()
    open('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_sent.txt','a').close()
    open('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Jpg_sent.jpg','a').close()
    tb1 = top_block_cls_1()
    tb1.Start()
    count_number = 1
    filesize = 0
    filesize_1 = 0
    filesize_2 = 0
    while 1:
	command = os.path.getsize('/home/spring2021/Desktop/Gnu radio code/backup2/Command.txt')
	filesize = os.path.getsize('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_sent.txt')
	if filesize != 0:	 ## have not blank txt
		if command == 0: ## send the txt
			tb2 = top_block_cls_2()
        		tb2.start()
			time.sleep(1)
			tb2.stop()
			os.remove('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_sent.txt')
	     		open('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_sent.txt','a').close()
			print('  :  txt sent')
	filesize_1 = os.path.getsize('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Jpg_sent.jpg')
	if filesize_1 !=0 :   ## have not blank jpg
		if command != 0: ## send the jpg
			tb3 = top_block_cls_4()
			tb3.start()
			time.sleep(10)
			tb3.stop()
			os.remove('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Jpg_sent.jpg')
			open('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Jpg_sent.jpg','a').close()
			print('  :  pic sent')
                
	filesize_2 = os.path.getsize('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_rec.txt')
	if filesize_2 != 0:
		if count_number > 1 :
			os.remove('/home/spring2021/Desktop/Gnu radio code/backup2/Receive_Overwrite.txt') 
		open('/home/spring2021/Desktop/Gnu radio code/backup2/Receive_Overwrite.txt','a').close()
		textFile = '/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Received_all/Receiver_%s.txt' % count_number
		shutil.move('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_rec.txt', textFile)
		open('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_rec.txt','a').close()
		time.sleep(1)
		with open('/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Received_all/Receiver_%s.txt' % count_number,'r') as firstfile, open('/home/spring2021/Desktop/Gnu radio code/backup2/Receive_Overwrite.txt','w') as secondfile: 
   		 # read content from first file
    			for line in firstfile: 
             		# write content to second file 
             			secondfile.write(line)
			secondfile.close()
		
		print ('  :  get txt')
		tb1.stop()
		tb1 = top_block_cls_1()
		tb1.start()
		count_number += 1
    tb1.stop()



if __name__ == '__main__':
    main()

