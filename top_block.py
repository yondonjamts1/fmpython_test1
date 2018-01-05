#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jan  5 04:30:02 2018
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
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44.1e3
        self.mpk_rate = mpk_rate = 160e3
        self.fm_rate = fm_rate = 640e3

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(640e3)
        self.uhd_usrp_sink_0.set_center_freq(200e6, 0)
        self.uhd_usrp_sink_0.set_gain(60, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=1600,
                decimation=441,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=1600,
                decimation=441,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=4,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_KAISER, #wintype
        	88e6, #fc
        	160e3, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.low_pass_filter_2 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, 44.1e3, 12e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, 44.1e3, 12e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 640e3, 60e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/lab-129/Downloads/cartoon010.wav', True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.330, ))
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_1 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, 160e3, 23e3, 53e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, 160e3, 100, 15e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0 = analog.sig_source_f(mpk_rate, analog.GR_COS_WAVE, 19000, 1, 0)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(2.5)
        self.analog_fm_preemph_1 = analog.fm_preemph(fs=samp_rate, tau=75e-6, fh=-1)
        self.analog_fm_preemph_0 = analog.fm_preemph(fs=samp_rate, tau=75e-6, fh=-1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_preemph_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.analog_fm_preemph_1, 0), (self.low_pass_filter_2, 0))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 2))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.analog_fm_preemph_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.analog_fm_preemph_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.low_pass_filter_2, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.low_pass_filter_2, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.band_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_multiply_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_mpk_rate(self):
        return self.mpk_rate

    def set_mpk_rate(self, mpk_rate):
        self.mpk_rate = mpk_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.mpk_rate)

    def get_fm_rate(self):
        return self.fm_rate

    def set_fm_rate(self, fm_rate):
        self.fm_rate = fm_rate


def main(top_block_cls=top_block, options=None):

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
