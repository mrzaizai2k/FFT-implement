# Implementations, Applications, and Case Studies:
1. Implement the algorithm in your preferred programming language(s).
2. Explore different implementation techniques, trade-offs, and optimizations.

[Data reordering, bit reversal, and in-place algorithms](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm#Data_reordering,_bit_reversal,_and_in-place_algorithms)

Although the abstract Cooley–Tukey factorization of the DFT, above, applies in some form to all implementations of the algorithm, much greater diversity exists in the techniques for ordering and accessing the data at each stage of the FFT. Of special interest is the problem of devising an in-place algorithm that overwrites its input with its output data using only O(1) auxiliary storage.

The best-known reordering technique involves explicit bit reversal for in-place radix-2 algorithms. Bit reversal is the permutation where the data at an index n, written in binary with digits b4b3b2b1b0 (e.g. 5 digits for N=32 inputs), is transferred to the index with reversed digits b0b1b2b3b4 . Consider the last stage of a radix-2 DIT algorithm like the one presented above, where the output is written in-place over the input: when are interleaved in the even and odd elements, corresponding to the least significant bit b0. Thus, in order to get the output in the correct place, b0 should take the place of b4 and the index becomes b0b4b3b2b1. And for next recursive stage, those 4 least significant bits will become b1b4b3b2, If you include all of the recursive stages of a radix-2 DIT algorithm, all the bits must be reversed and thus one must pre-process the input (or post-process the output) with a bit reversal to get in-order output. (If each size-N/2 subtransform is to operate on contiguous data, the DIT input is pre-processed by bit-reversal.) Correspondingly, if you perform all of the steps in reverse order, you obtain a radix-2 DIF algorithm with bit reversal in post-processing (or pre-processing, respectively).

The logarithm (log) used in this algorithm is a base 2 logarithm.

3. Benchmark your implementations against other algorithms or existing libraries.

My way is to do the memoization 

Memoization, in the context of dynamic programming, is a technique used to optimize the performance of recursive algorithms by storing the results of expensive function calls and returning the cached result when the same inputs occur again. In the case of the Fast Fourier Transform (FFT), memoization can be applied to store intermediate results of complex exponential calculations, thereby avoiding redundant computations and significantly improving the overall performance

- Avoiding Redundant Computations:

In FFT, one of the most computationally expensive operations is the calculation of complex exponential factors for each frequency bin.
When performing FFT recursively, the same complex exponential factors are often computed multiple times for the same inputs.
Memoization stores the results of these complex exponential calculations in a cache, ensuring that if the same inputs are encountered again, the precomputed result can be directly retrieved from the cache instead of recomputing it.
By avoiding redundant computations, memoization reduces the overall time complexity of the FFT algorithm.

- Optimizing Recursive Calls:

FFT involves recursive calls to compute FFT for smaller subproblems, such as even-indexed and odd-indexed samples.
Each recursive call requires computing complex exponential factors and combining the results of subproblems.
Memoization optimizes these recursive calls by storing the results of intermediate FFT computations.
When a subproblem with the same inputs is encountered again during recursion, the cached result can be retrieved, eliminating the need to recompute the FFT for that subproblem.
This optimization reduces the number of function calls and computational overhead, leading to faster execution of the FFT algorithm.

- Dynamic Programming Approach:

Memoization in FFT can be viewed as a form of dynamic programming, where the problem is broken down into smaller subproblems, and the results of subproblems are stored in a table (cache) to avoid redundant computations.
By applying memoization, FFT transforms from a purely recursive algorithm to a dynamic programming approach, where solutions to subproblems are reused to compute solutions to larger problems.
This dynamic programming approach with memoization significantly improves the efficiency of FFT, especially for large input sizes, as it minimizes the computational overhead associated with repeated calculations.

We use memoization to cache the `w = np.exp(-2j * np.pi * k / size)`

The benchmark. We implement FFT to figure out the frequency of the sound wave. we compare the memoization FFT to the original FFT, FFT implemented by numpy and DFT

The graph below shows the frequency graph for an input wave file made up of a single 440hz sine wave.

![A graph with the frequencies from 0hz to 20050hz plotted along the x-axis (the frequency domain) and the magnitude plotted along the y-axis (the amplitude or magnitude, i.e. the contribution this frequency makes to the signal). The graph spikes at 440hz, showing 440hz as the dominant frequency](docs/new_result.jpg)

As we can see the DFT has the lowest speed, the original FFT takes 0.017s to perform, my memoization version implemented it 10x faster. and the best speed is numpy FFT as it's written mainly in C language.

However, The numpy took used 32880 bytes of memory, while memoization and original FFT used 16440 bytes of memory to perform


- Investigate real-world applications of algorithms in various fields such as computer science, engineering, finance, and more to gain practical experience.
- Understand how the algorithm solves specific problems in these domains.
- Study case examples where the algorithm has been used to solve complex problems.
- Analyze the strategies and adaptations applied in these cases.
