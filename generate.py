
from sys import argv, stderr

import data
from slicenostics import slicenostics

# this is the main script to create the slicenostics 
# measurements from a run file

if __name__ == '__main__':
  if len(argv) != 3:
    stderr.write("usage: python generate.py <input file> <output file>")
    exit(1)

  ds = data.load(argv[1])
  sn = slicenostics(ds)
  sn.to_csv(argv[2], index=False)

