import numpy as np
from scipy.special import erfc

def Q(x):
    return 0.5 * erfc(x / np.sqrt(2))