import numpy as np

def rrc(t: float, alpha: float, T: float) -> np.ndarray:
    """
        function def
            Generates the impulse response, h(t), of a RRC filter

        INPUT: 
            - t: Time vector at which to evaluate the RRC filter impulse response, h(t).
            - alpha: Roll-off factor of RRC filter (0<=alpha<=1)
            - T: Symbol period (T=1/Rs)
        OUTPUT: 
            - h: Impulse response of RCC filter, denoted as h(t) in time domain
    """

    h = np.zeros_like(t)

    for i in range(len(t)):
        if t[i] == 0:
            h[i] = (1 + alpha * (4 / np.pi - 1)) / T
        elif t[i] == T / (4 * alpha) or t[i] == -T / (4 * alpha):
            h[i] = (alpha / T / np.sqrt(2)) * ((1 + 2 / np.pi) * np.sin(np.pi / (4 * alpha)) +
                   (1 - 2 / np.pi) * np.cos(np.pi / (4 * alpha)))
        else:
            num = (np.sin(np.pi * t[i] / T * (1 - alpha)) +
                        (4 * alpha * t[i] / T) * np.cos(np.pi * t[i] / T * (1 + alpha)))
            denom = (np.pi * t[i] * (1 - (4 * alpha * t[i] / T)**2))
            h[i] = num / denom

    return h

