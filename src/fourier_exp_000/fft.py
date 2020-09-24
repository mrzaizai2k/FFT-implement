# -*- coding: utf-8 -*-

import argparse
import sys
import logging
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wav

from fourier_exp_000 import __version__

__author__ = "Lisa Burton"
__copyright__ = "Lisa Burton"
__license__ = "mit"

_logger = logging.getLogger(__name__)

def parse_args(args):
    parser = argparse.ArgumentParser(
        description="Just a Discrete Fourier Transform (DFT) demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="fourier-exp-000 {ver}".format(ver=__version__))
    parser.add_argument(
        dest="input_file",
        help="input wave file to perform DFT against",
        type=str,
        metavar="INPUT")
    parser.add_argument(
      "--frequency-max",
      dest="frequency_max",
      help="maximum frequency range in hertz (Hz)",
      type=int,
      default=1000
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)

def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")

def my_fft(sample_set, constant):
    if len(sample_set) == 1:
        return sample_set

    if len(sample_set) % 2 != 0:
        print("{} must be a power of 2".format(len(sample_set)))

    size = len(sample_set)
    even_fft = my_fft(sample_set[0::2], size)
    odd_fft = my_fft(sample_set[1::2], size)

    freq_bins = [0.0] * size
    for k in range(0, int(size / 2)):
        freq_bins[k] = even_fft[k]
        freq_bins[k + int(size / 2)] = odd_fft[k]

    for k in range(0, int(size / 2)):
        e = np.exp(-2j * np.pi * k / size)
        t = freq_bins[k]
        freq_bins[k] = t + e * freq_bins[k + int(size / 2)]
        freq_bins[k + int(size / 2)] = t - e * freq_bins[k + int(size / 2)]

    return freq_bins

def discrete_fourier_transform(sample_set, freq_max):
    transform_vector = [0j] * freq_max

    print("Transforming from the time domain to frequency domain...")
    for n in range(0, freq_max):
        for m in range(0, freq_max):
            transform_vector[m] = transform_vector[m] + (sample_set[n] * np.exp(-2j * np.pi * n * m / freq_max))

    return transform_vector

def scale_for_graph(transform_vector, output_size):
    output = [0.0] * output_size

    scaler = len(transform_vector) / output_size
    for i in range(0, output_size):
        output[i] = abs(transform_vector[int(scaler * i)])

    return output

def main(args):
    args = parse_args(args)
    setup_logging(args.loglevel)

    window_size = 2 ** 11
    rate, sampleset = wav.read(args.input_file)
    sampleset = sampleset[:window_size]

    print("Closing {}".format(args.input_file))

    start = time.time()
    freq_bins_my_fft = my_fft(sampleset, window_size)
    end = time.time()
    my_fft_time = round(end - start, 2)

    start = time.time()
    freq_bins_numpy_fft = np.fft.fft(sampleset, window_size)
    end = time.time()
    np_fft_time = round(end - start, 2)

    start = time.time()
    freq_bins_my_dft = scale_for_graph(discrete_fourier_transform(sampleset, window_size), window_size)
    end = time.time()
    my_dft_time = round(end - start, 2)

    fig, axs = plt.subplots(3, 1)
    axs[0].set_title('My FFT (Cooley-Tukey) [time={}]'.format(my_fft_time))
    axs[0].set_xlabel('Frequency (Hz)')
    axs[0].set_ylabel('Bin size')
    axs[0].plot(np.arange(22050), scale_for_graph(freq_bins_my_fft[:len(freq_bins_my_fft) // 2], 22050))
    
    axs[1].set_title('Numpy FFT [time={}]'.format(np_fft_time))
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Bin size')
    axs[1].plot(np.arange(22050), scale_for_graph(freq_bins_numpy_fft[:len(freq_bins_numpy_fft) // 2], 22050))
    
    axs[2].set_title('My DFT (Brute force) [time={}]'.format(my_dft_time))
    axs[2].set_xlabel('Frequency (Hz)')
    axs[2].set_ylabel('Bin size')
    axs[2].plot(np.arange(22050), scale_for_graph(freq_bins_my_dft[:len(freq_bins_numpy_fft) // 2], 22050))

    fig.tight_layout()
    plt.show()

def run():
    main(sys.argv[1:])

if __name__ == "__main__":
    run()
