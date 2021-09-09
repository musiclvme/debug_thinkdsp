from thinkdsp import Chirp
from thinkdsp import ExpoChirp
from thinkdsp import SinSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import os

def find_index(x, xs):
    """Find the index corresponding to a given value in an array."""
    n = len(xs)
    start = xs[0]
    end = xs[-1]
    i = round((n - 1) * (x - start) / (end - start))
    return int(i)

def test_Chirp():
    pathdir_out = "chap3_out"
    if not os.path.exists(pathdir_out):
        try:
            os.makedirs(pathdir_out)
        except:
            pass
    wavfilename = pathdir_out + "/Chirp.wav"
    signal = Chirp(start=220, end=880)
    wave1 = signal.make_wave(duration=2)
    wave1.segment(start=0, duration=0.05).plot()
    decorate(xlabel='Time (s)')
    wave1.write(wavfilename)

def test_ExpoChirp():
    pathdir_out = "chap3_out"
    if not os.path.exists(pathdir_out):
        try:
            os.makedirs(pathdir_out)
        except:
            pass
    wavfilename = pathdir_out + "/ExpoChirp.wav"
    signal = ExpoChirp(start=220, end=880)
    wave2 = signal.make_wave(duration=2)
    wave2.write(wavfilename)

def test_leak():
    signal = SinSignal(freq=440)
    duration = signal.period * 30
    wave = signal.make_wave(duration)
    #wave.plot()
    #decorate(xlabel='Time (s)')

    spectrum = wave.make_spectrum()
    #spectrum.plot(high=880)
    #decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')

    duration2 = signal.period * 30.25
    wave2 = signal.make_wave(duration2)
    #wave2.plot()
    #decorate(xlabel='Time (s)')

    spectrum2 = wave2.make_spectrum()


    #plot all you need in on figure
    plt.figure()
    plt.subplot(3, 2, 1)
    plt.plot(wave.ts, wave.ys)

    plt.subplot(3, 2, 2)
    i = find_index(880, spectrum.fs)
    plt.plot(spectrum.fs[:i], spectrum.amps[:i])

    plt.subplot(3, 2, 3)
    plt.plot(wave2.ts, wave2.ys)

    plt.subplot(3, 2, 4)
    i = find_index(880, spectrum2.fs)
    plt.plot(spectrum2.fs[:i], spectrum2.amps[:i])

    wave2.hamming()
    spectrum2 = wave2.make_spectrum()

    plt.subplot(3, 2, 5)
    plt.plot(wave2.ts, wave2.ys)

    plt.subplot(3, 2, 6)
    i = find_index(880, spectrum2.fs)
    plt.plot(spectrum2.fs[:i], spectrum2.amps[:i])
    plt.show()


def plot_spectrogram(wave, seg_length):
    """
    """
    spectrogram = wave.make_spectrogram(seg_length)
    print('Time resolution (s)', spectrogram.time_res)
    print('Frequency resolution (Hz)', spectrogram.freq_res)
    spectrogram.plot(high=700)
    decorate(xlabel='Time(s)', ylabel='Frequency (Hz)')

def test_spectrum():
    signal = Chirp(start=220, end=440)
    wave = signal.make_wave(duration=1)
    spectrum = wave.make_spectrum()
    spectrum.plot(high=700)
    decorate(xlabel='Frequency (Hz)')

    signal = Chirp(start=220, end=440)
    wave = signal.make_wave(duration=1, framerate=11025)
    plot_spectrogram(wave, 512)



if __name__ == "__main__":
    #test_Chirp()
    #test_ExpoChirp()
    #test_leak()
    test_spectrum()