import thinkdsp
from thinkdsp import read_wave
from thinkdsp import SinSignal
import os
import matplotlib.pyplot as plt


def filter_wave(wave, start, duration, cutoff):
    """Selects a segment from the wave and filters it.

    Plots the spectrum and displays an Audio widget.

    wave: Wave object
    start: time in s
    duration: time in s
    cutoff: frequency in Hz
    """
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')
    spectrum.low_pass(cutoff)
    spectrum.plot(high=5000, color='#045a8d')
    thinkdsp.decorate(xlabel='Frequency (Hz)')

    audio = spectrum.make_wave()
    return audio

def test_stretch():
    pathdir_out = "chap1_out"
    wave = read_wave('170255__dublie__trumpet.wav')
    wave.normalize()

    wave1 = wave.copy()

    factor = 0.5

    wave1.ts *= factor
    wave1.framerate /= factor

    #wave.plot()
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(wave.ts, wave.ys)

    plt.subplot(2,1,2)
    plt.plot(wave1.ts, wave1.ys)
    plt.show()

    wavefilename = pathdir_out + "/stretch_wave_normal.wav"
    wave1filename = pathdir_out + "/stretch_wave_speed.wav"
    wave.write(wavefilename)
    wave1.write(wave1filename)

def test_signal():
    pathdir_out = "chap1_out"
    signal = (SinSignal(freq=400, amp=1.0) +
              SinSignal(freq=600, amp=0.5) +
              SinSignal(freq=800, amp=0.25))
    signal.plot()

    wave2 = signal.make_wave(duration=1)
    wave2.apodize()
    wavfilename = pathdir_out + "/wave_400_600_800.wav"
    wave2.write(wavfilename)

    spectrum = wave2.make_spectrum()
    #spectrum.plot(high=2000)
    fig1 = pathdir_out + "/wave_400_600_800.jpg"
    spectrum.plot_writefile(high=2000, filename=fig1)


def test_basics():
    # test out dir
    pathdir_out = "chap1_out"

    if not os.path.exists(pathdir_out):
        try:
            os.makedirs(pathdir_out)
        except:
            pass
    # read file
    wave = read_wave('170255__dublie__trumpet.wav')
    wave.normalize()

    # make_audio is only for notebook
    # wave.make_audio()

    # draw wave
    fig1 = pathdir_out + "/wav.jpg"
    # wave.plot()
    wave.plot_writefile(fig1)

    #
    fig2 = pathdir_out + "/segment.jpg"
    segment = wave.segment(start=1.1, duration=0.3)
    # segment.plot()
    segment.plot_writefile(fig2)

    segment.segment(start=1.1, duration=0.005).plot()

    # freq
    fig3 = pathdir_out + "/spec_7000.jpg"
    spectrum = segment.make_spectrum()
    spectrum.plot_writefile(high=7000, filename=fig3)

    peaks = spectrum.peaks()[:30]
    print(peaks)

    # low pass wave
    wavfilename = pathdir_out + "/lowpass_2000.wav"
    spectrum.low_pass(2000)
    wavfile = spectrum.make_wave()
    wavfile.write(wavfilename)

    wavfilename = pathdir_out + "/filter_5000.wav"
    fig4 = pathdir_out + "/filter_5000.jpg"
    filter_wav = filter_wave(wave, start=0, duration=5, cutoff=5000)
    filter_wav.plot_writefile(fig4)
    filter_wav.write(wavfilename)

if __name__ == "__main__":
    #test_signal()
    test_stretch()









