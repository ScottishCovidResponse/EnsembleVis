
import pandas as pd

from analysis import *

# slicenostics routines for each of the different runs

def slicenostics(ds):
  mx = maxinfections(ds)
  mn = mininfections(ds)
  linfits = polyfits(ds, 1)
  quadfits = polyfits(ds, 2)

  # creates a new data frame with the slicenostics result for each run
  df = pd.DataFrame({
    'average': average(ds),
    'wiggliness': variability(ds),
    'straightness': np.array([m[1][0] for m in linfits]),
    'prominence': mx - mn,
    'sinuosity': arclength(ds) / 365.0, # FIXME: if cols change change this!
    'steepness': np.array([m[0][0] for m in linfits]),
    'monotonic_inc': (monotonic(ds) + 1.0) / 2.0,
    'monotonic_dec': (-monotonic(ds) + 1.0) / 2.0,
    'gain': ttlgain(ds),
    'loss': ttlloss(ds),
    #'curvature': # ???,
    'bowlness': np.array([m[1][0] for m in quadfits]),
    'symmetry': skewness(ds),
    'peakiness': kurtosis(ds)
  })

  return df
