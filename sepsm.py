from __future__ import division, print_function
import numpy as np
import scipy as sp
import scipy.io.wavfile
import general
import filterbank
import auditory
import distort


MIDFREQ = (63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000,
           1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000)
HT_DIFFUSE = (37.5, 31.5, 26.5, 22.1, 17.9, 14.4, 11.4, 8.4, 5.8, 3.8, 2.1,
              1.0, 0.8, 1.9, 0.5, -1.5, -3.1, -4.0, -3.8, -1.8, 2.5, 6.8)
FS = 22050.0


def auditory_processing(signal, center_f=MIDFREQ, fs=FS):
    # Gammatone filering
    b, a, _, _, _ = auditory.gammatone_make(fs, center_f)
    y = auditory.gammatone_apply(signal, b, a)
    return general.hilbert_envelope(y)

