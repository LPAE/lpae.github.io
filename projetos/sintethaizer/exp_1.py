import numpy as np
from scipy import signal as sg
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100
t = 4.0

input = np.ones(int(t*fs))

tom_la = 110


def irr_filter(buffer_array,
               n=10,
               wn=(300*np.pi, 600*np.pi),
               rs=60,
               btype='bandstop',
               ftype='cheby2'):

    [b, a] = sg.iirfilter(  int(n),
                            wn=wn,
                            rs=rs,
                            btype=btype,
                            analog=True,
                            ftype=ftype)

    return sg.lfilter(b, a, buffer_array)


def dc_offset(ampl=1, t=4.0, fs=44100):
    _sample_array = np.linspace(0, t, num=int(t*fs))
    return ampl*np.ones(int(t*fs))


def sin_envelop(buffer_array, tom, ampl=1, t=4.0, fs=44100):
    _sample_array = np.linspace(0, t, num=int(t*fs))
    return ampl*buffer_array*np.sin(2*np.pi*tom*_sample_array)


def square_envelop(buffer_array, tom, ampl=1, t=4.0, fs=44100, duty=0.5):
    _sample_array = np.linspace(0, t, num=int(t*fs))
    return ampl*buffer_array*sg.square(2*np.pi*tom*_sample_array, duty=duty)


def sawtooth_envelop(buffer_array, tom, ampl=1, t=4.0, fs=44100):
    _sample_array = np.linspace(0, t, num=int(t*fs))
    return ampl*buffer_array*sg.sawtooth(2*np.pi*tom*_sample_array)


def step_envelop(buffer_array, tom, ampl=1, t=4.0, fs=44100, duty=0.5):
    _sample_array = np.linspace(0, t, num=int(t*fs))
    return ampl*buffer_array*(sg.square(2*np.pi*tom*_sample_array, duty=duty)+dc_offset())/2


def ramp_envelop(buffer_array, tom, ampl=1, t=4.0, fs=44100):
    _sample_array = np.linspace(0, t, num=int(t*fs))
    return ampl*buffer_array*(sg.sawtooth(2*np.pi*tom*_sample_array)+dc_offset())/2


buffer = input;

buffer = step_envelop(buffer, 4, duty=0.7)
buffer = ramp_envelop(buffer, 3)
buffer = sin_envelop(buffer, tom_la)
buffer = sin_envelop(buffer, 1)
buffer = irr_filter(buffer)
#buffer = irr_filter(buffer, Wn=((np.pi/4), (3*np.pi/4)),  btype='band')

output = buffer
plt.plot(output)
plt.show()

sd.default.samplerate = fs
sd.play(output, loop=True)
sd.wait()

