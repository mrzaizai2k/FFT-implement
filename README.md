# In-place Cooley-Tukey FFT implementation

*This is a toy FFT implementation. Numpy has a fantastic production quality implementation*

Note: [Source code is here](https://github.com/spacekitcat/cooley-tukey-fast-fourier-transform/blob/master/src/fourier_exp_000/fft.py), sorry about all the boiler plate, I used some project generator and shouldn't have!

Note2: I used memoization to decrease the speed FFT. Big thanks to the original repo

Fourier transforms are really cool and I want to learn the maths and concepts behind it all. This continues from [fourier-exp-01](https://github.com/spacekitcat/fourier-exp-01), a small C program that performs a temporal to frequency domain transform. This is a port of the C program, Python seems to have a better selection of libraries for parsing wave files, drawing graphs and doing maths.

This project includes a Python implementation of the Discrete Fourier Transform (DFT) in the C project above, it also contains an
implementation of the Cooley-Tukey Fast Fourier Transform (FFT). The key differences between this project and the earlier C project is that this one uses Python's built in support for complex numbers, it also uses the correct divisor in the argument for the complex exponent operation (which expands [cis(x)](https://en.wikipedia.org/wiki/Cis_(mathematics))).

## Building

```bash
git clone github.com/spacekitcat/<repository-name>
cd <repository-name>
python setup.py develop
python src/fourier_exp_000/fft.py resources/440hz.wav
```

The graph below shows the frequency graph for an input wave file made up of a single 440hz sine wave.

![A graph with the frequencies from 0hz to 20050hz plotted along the x-axis (the frequency domain) and the magnitude plotted along the y-axis (the amplitude or magnitude, i.e. the contribution this frequency makes to the signal). The graph spikes at 440hz, showing 440hz as the dominant frequency](docs/new_result.jpg)


The graph below shows the frequency graph for an input wave file made up of a 500hz and a 1200hz sine wave.

![A graph with the frequencies from 0hz to 20050hz plotted along the x-axis (the frequency domain) and the magnitude plotted along the y-axis (the amplitude or magnitude, i.e. the contribution this frequency makes to the signal). The graph spikes at 500hz and 1200hz, showing 500hz and 1200hz as the dominant frequencies](docs/500hz-1200hz-example.png)

## Learning Material

[Fourier Series (Dover Books on Mathematics) - Georgi P. Tolstov](https://www.amazon.co.uk/gp/product/B008TVG4ES/ref=ppx_yo_dt_b_d_asin_title_o01?ie=UTF8&psc=1)

[Wikipedia: Cooley–Tukey FFT algorithm](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm)
