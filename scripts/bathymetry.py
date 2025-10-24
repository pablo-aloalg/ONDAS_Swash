import numpy as np
import matplotlib.pyplot as plt

def linear_profile(h0, Ltotal, Wconst=0.0, slope=None, hFinal=None, dx=1.0):

    if slope is None and hFinal is None:
        raise ValueError("Either slope or hFinal must be provided.")
    if slope is not None and hFinal is not None:
        raise ValueError("Provide only one of slope or hFinal, not both.")

    
    # Total number of points
    N = int(Ltotal / dx) + 1
    x = np.linspace(0, Ltotal, N)
    z = np.zeros_like(x)
    
    # Index where the slope starts
    idx_slope_start = int(Wconst / dx)
    
    # Constant depth section
    z[:idx_slope_start] = h0
    
    # Linear section
    x_slope = x[idx_slope_start:]
    
    if slope is not None:
        z[idx_slope_start:] = h0 + slope * (x_slope - Wconst)
    else:
        # compute slope automatically
        slope_auto = (hFinal - h0) / (Ltotal - Wconst)
        z[idx_slope_start:] = h0 + slope_auto * (x_slope - Wconst)
    
    return x, z