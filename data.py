import numpy as np
import pandas as pd
import h5py

# returns a pandas data frame with text integers specifying the index and 
# labels for which intervention and series
def load(filename):
  data = h5py.File(filename, 'r')

  pddata = pd.DataFrame(columns=['intervention', 'series'])

  for group in data.keys():
    s = group.split('_')
    intervention, series = s[0], s[1]

    for dset in data[group]:
      #ds_data = data[group][dset] # there seems to be only 1 of these
      arr = data[group][dset][:] # adding [:] returns a numpy array
      df = pd.DataFrame(arr)
      df['intervention'] = intervention
      df['series'] = series

    # add everything to the main data frame
    pddata = pddata.append(df)

  pddata.reindex() # fix pandas numbering
  return pddata

