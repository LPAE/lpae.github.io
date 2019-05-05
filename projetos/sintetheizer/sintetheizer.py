import numpy as np
from scipy import signal as sg
import sounddevice as sd
import matplotlib.pyplot as plt


class Sintetheizer:
    def __init__(self,
                 buffer_array=None,
                 fs=44100,
                 t=4.0,
                 ):

        if buffer_array is None:
            self.buffer_array = np.ones(int(t*fs), dtype=np.float32)

        else:
            self.buffer_array = buffer_array

        self.fs = fs
        self.t = t

    def irr_filter(self,
                   n=10,
                   wn=((np.pi / 4), (3 * np.pi / 4)),
                   rs=60,
                   btype='bandstop',
                   ftype='cheby2'):

            [b, a] = sg.iirfilter(int(n),
                                  Wn=wn,
                                  rs=rs,
                                  btype=btype,
                                  analog=True,
                                  ftype=ftype)

            self.buffer_array = sg.lfilter(b, a, self.buffer_array)

    def lowpass(self,
                N=4,
                cutoff=0.01):

      b, a = sg.butter(N, cutoff, analog=False)

      # w, h = sg.freqs(b, a)
      # plt.semilogx(w, 20 * np.log10(abs(h)))
      # plt.show()

      self.buffer_array = sg.filtfilt(b, a, self.buffer_array)


    def dc_offset(self,
                  ampl=1):

        _sample_array = np.linspace(0, self.t, num=int(self.t * self.fs))
        self.buffer_array = ampl * np.ones(int(self.t * self.fs)) + self.buffer_array

    def sin_envelop(self,
                    tom,
                    ampl=1.0):

        _sample_array = np.linspace(0, self.t, num=int(self.t * self.fs))
        self.buffer_array = self.buffer_array*ampl*np.sin(2*np.pi*tom*_sample_array)

    def square_envelop(self,
                       tom,
                       ampl=1.0,
                       duty=0.5):

        _sample_array = np.linspace(0, self.t, num=int(self.t * self.fs))
        self.buffer_array = self.buffer_array*ampl*sg.square(2*np.pi*tom*_sample_array, duty=duty)

    def sawtooth_envelop(self,
                         tom,
                         ampl=1.0):

        _sample_array = np.linspace(0, self.t, num=int(self.t * self.fs))
        self.buffer_array = self.buffer_array*ampl*sg.sawtooth(2*np.pi*tom*_sample_array)

    def step_envelop(self,
                     tom,
                     ampl=1.0,
                     duty=0.5):

        _sample_array = np.linspace(0, self.t, num=int(self.t * self.fs))
        _step = sg.square(2*np.pi*tom*_sample_array, duty=duty)
        _step = _step + np.ones(int(self.t*self.fs), dtype=np.float32)
        _step = ampl*_step/2

        self.buffer_array = self.buffer_array*_step

    def ramp_envelop(self,
                     tom,
                     ampl=1.0):

        _sample_array = np.linspace(0, self.t, num=int(self.t * self.fs))
        self.buffer_array = self.buffer_array*ampl*(
                sg.sawtooth(2*np.pi*tom*_sample_array) + self.dc_offset()
        )/2

    def plot_wave(self):
        plt.plot(self.buffer_array)
        plt.show()

    def play_sound(self, loop=True):
        sd.default.samplerate = self.fs
        sd.play(self.buffer_array, loop=loop)
        sd.wait()

    def stop_sound(self):
        sd.default.samplerate = self.fs
        sd.stop()






