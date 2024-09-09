import numpy as np

def qpskdetect(x):
    """
    function def
        This function takes in a vector of complex numbers x, representing 
        the received signal after passing through a matched filter.

        sign(x) returns 1 if x > 0 and returns -1 if x < 0.

        For a complex vector x, real(x) and imag(x) return vectors containing 
        the real and imaginary parts of x, respectively. 

        I and Q are vectors that map the real and imaginary parts of the 
        received signal x into binary values where 0 -> -1 and 1 -> 1. 

        The odd entries of 'bits' are derived from the real component vector I,
        and the even entries of 'bits' are derived from the imaginary component vector Q.

    INPUT: 
        - x: Received downsample signal (complex vector)
    OUTPUT: 
        - symbols: Decoded QPSK symbols with normalized energy Es=1
        - bits: Decoded bit sequence (binary vector)
    """
    I = np.sign(np.real(x))
    Q = np.sign(np.imag(x))

    symbols = (I + 1j * Q)/np.sqrt(2)
    bits = np.zeros(2*len(x),dtype=int)
    bits[0::2] = (I+1)/2
    bits[1::2] = (Q+1)/2

    return symbols, bits