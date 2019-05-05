import sintetheizer.Sintetheizer as 

sint_1 = Sintetheizer()

# sint_1.sawtooth_envelop(110.0, ampl=1)
# sint_1.sawtooth_envelop(220.0, ampl=1.2)
#

sint_1.sawtooth_envelop(55)

# sint_1.sin_envelop(3, ampl=1.5)
# sint_1.sin_envelop(4, ampl=1.5)
# sint_1.sin_envelop(4, ampl=1.5)

# sint_1.step_envelop(8, ampl=1.1, duty=0.6)

sint_1.sin_envelop(1, ampl=2)

sint_1.step_envelop(1, duty=0.75)
sint_1.step_envelop(3, duty=0.75)
sint_1.step_envelop(8, duty=0.50)

# sint_1.sin_envelop(0.125, ampl=1.1)

sint_1.lowpass()

sint_1.plot_wave()
sint_1.play_sound(loop=True)