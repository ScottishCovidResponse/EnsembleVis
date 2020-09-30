import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# functions to support analysis.

def maxinfections(d):
  return np.amax(d, axis=1)

def mininfections(d):
  return np.amin(d, axis=1)

def average(d):
  return np.mean(d, axis=1)

def variability(d):
  return np.var(d, axis=1) / np.std(d, axis=1)

def skewness(d):
  dd = runs(d)
  return stats.skew(dd, axis=1)

def kurtosis(d):
  dd = runs(d)
  return stats.kurtosis(dd, axis=1)

# total distance along the line
def arclength(r):
  dd = runs(r)
  changes = dd.iloc[:,1:].values - dd.iloc[:,:-1].values
  lengs = np.sqrt(np.abs(changes) + 1) # each step is 1 in this dataset
  return np.sum(lengs, axis=1)

def polyfits(r, deg): # returns a list of polynomial models for each row in r
  dd = runs(r)
  X = list(range(dd.shape[1]))
  fit = np.polyfit
  #fit = np.polynomial.polynomial.Polynomial.fit # better numerics apparently
  return [fit(X, row.values, deg, full=True) for index, row in dd.iterrows()]

def pca2d(d):
  x = StandardScaler().fit_transform(runs(d))
  pca = PCA(n_components=2) # we could extract more coefficients, here is for ploting on 2d space
  pcs = pca.fit_transform(x)
  return pcs

def monotonic(r):
  # returns the percentage of times the curve increases in value
  dd = runs(r)
  changes = dd.iloc[:,1:].values - dd.iloc[:,:-1].values
  ttl = np.sum(np.sign(changes), axis=1) # value between -1 and 1
  return ttl / dd.shape[1] # percentage as number of cols

def ttlgain(r):
  # analogy to climbing height in biking/hiking/running/etc
  # total height gained ignoring going down
  dd = runs(r)
  changes = dd.iloc[:,1:].values - dd.iloc[:,:-1].values
  changes[changes<=0] = 0
  return np.sum(changes, axis=1)

def ttlloss(r):
  # analogy to climbing height in biking/hiking/running/etc
  # total height lost ignoring going up
  dd = runs(r)
  changes = dd.iloc[:,1:].values - dd.iloc[:,:-1].values
  changes[changes>=0] = 0
  return np.sum(changes, axis=1)

def runs(r):
  return r[[str(i) for i in range(1,367)]]

