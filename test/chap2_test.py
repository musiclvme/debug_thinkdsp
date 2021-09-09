
from thinkdsp import TriangleSignal
from thinkdsp import SquareSignal
from thinkdsp import SawtoothSignal
from thinkdsp import decorate

def test_triangle():

    signal = TriangleSignal(200)
    duration = signal.period*3
    segment = signal.make_wave(duration, framerate=10000)
    segment.plot()
    decorate(xlabel='Time (s)')

    wave = signal.make_wave(duration=0.5, framerate=10000)
    wave.apodize()
    spectrum = wave.make_spectrum()
    spectrum.plot()
    decorate(xlabel='Frequency (Hz)')

def test_square():
    signal = SquareSignal(200)
    duration = signal.period * 3
    segment = signal.make_wave(duration, framerate=10000)
    segment.plot()
    decorate(xlabel='Time (s)')

    wave = signal.make_wave(duration=0.5, framerate=10000)
    wave.apodize()
    spectrum = wave.make_spectrum()
    spectrum.plot()
    decorate(xlabel='Frequency (Hz)')

def test_Sawtooth():
    signal = SawtoothSignal(200)
    duration = signal.period * 3
    segment = signal.make_wave(duration, framerate=10000)
    segment.plot()
    decorate(xlabel='Time (s)')

    wave = signal.make_wave(duration=0.5, framerate=10000)
    wave.apodize()
    spectrum = wave.make_spectrum()
    spectrum.plot()
    decorate(xlabel='Frequency (Hz)')
if __name__ == "__main__":
    #test_triangle()
    #test_square()
    test_Sawtooth()